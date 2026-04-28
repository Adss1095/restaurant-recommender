from sklearn.preprocessing import MinMaxScaler
from difflib import get_close_matches


# 🔍 Find closest restaurant name
def find_closest_name(name, df):
    names = df['Restaurant Name'].tolist()
    match = get_close_matches(name, names, n=1, cutoff=0.5)
    return match[0] if match else None


# 🔥 Build hybrid scores
def build_hybrid_scores(df, cosine_sim):
    scaler = MinMaxScaler()

    df['Normalized Rating'] = scaler.fit_transform(df[['Aggregate rating']])
    df['Normalized Cost'] = scaler.fit_transform(df[['Average Cost for two']])

    df['Popularity Score'] = (
        0.7 * df['Normalized Rating'] +
        0.3 * (1 - df['Normalized Cost'])
    )

    return df


# 🤖 Main recommendation function
def hybrid_recommend(df, cosine_sim, user_input, top_n=5):

    user_input = user_input.lower().strip()

    # 🔥 Food → cuisine mapping
    food_map = {
        "milkshake": "cafe",
        "shake": "cafe",
        "juice": "cafe",
        "coffee": "cafe",
        "biryani": "north_indian",
        "pizza": "italian",
        "noodles": "chinese"
    }

    user_input = food_map.get(user_input, user_input)

    # ==============================
    # STEP 1: CUISINE MATCH
    # ==============================
    df['Cuisine_List'] = df['Cuisines'].apply(
        lambda x: [c.strip() for c in x.split(',')]
    )

    cuisine_matches = df[
        df['Cuisine_List'].apply(lambda x: user_input in x)
    ]

    if not cuisine_matches.empty:
        cuisine_matches = cuisine_matches.sort_values(
            by=['Aggregate rating', 'Average Cost for two'],
            ascending=[False, True]
        )

        results = []

        for _, row in cuisine_matches.head(top_n).iterrows():
            results.append({
                "name": row['Restaurant Name'],
                "rating": float(row['Aggregate rating']),
                "cost": float(row['Average Cost for two']),
                "score": 1.0
            })

        return {
            "input": user_input,
            "results": results
        }

    # ==============================
    # STEP 2: RESTAURANT MATCH
    # ==============================
    restaurant_name = find_closest_name(user_input, df)

    if not restaurant_name:
        return {
            "error": "No matching restaurants found",
            "results": []
        }

    idx = df[df['Restaurant Name'] == restaurant_name].index[0]

    # 🔥 SAFETY FIX (no crash now)
    if idx >= len(cosine_sim):
        return {
            "error": "Model mismatch error",
            "results": []
        }

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    candidates = [i[0] for i in sim_scores[1:top_n+10]]

    results = []

    for i in candidates:
        content_score = cosine_sim[idx][i]
        popularity_score = df.iloc[i]['Popularity Score']

        final_score = 0.6 * content_score + 0.4 * popularity_score

        results.append({
            "name": df.iloc[i]['Restaurant Name'],
            "rating": float(df.iloc[i]['Aggregate rating']),
            "cost": float(df.iloc[i]['Average Cost for two']),
            "score": round(float(final_score), 3)
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)[:top_n]

    return {
        "input": restaurant_name,
        "results": results
    }