import numpy as np

def precision_at_k(df, cosine_sim, hybrid_func, k=5, sample_size=50):
    correct = 0
    total = 0

    # Take random samples
    sample_df = df.sample(min(sample_size, len(df)))

    for _, row in sample_df.iterrows():
        input_name = row['Restaurant Name']
        input_cuisine = row['Cuisines']

        result = hybrid_func(df, cosine_sim, input_name, top_n=k)

        if "results" not in result:
            continue

        recommendations = result["results"]

        for rec in recommendations:
            rec_name = rec["name"]
            rec_cuisine = df[df['Restaurant Name'] == rec_name]['Cuisines'].values[0]

            # Check if cuisines overlap
            if any(c in rec_cuisine for c in input_cuisine.split(', ')):
                correct += 1

            total += 1

    precision = correct / total if total > 0 else 0
    return precision
