from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_content_model(df):
    # Clean cuisines
    df['Cuisines'] = df['Cuisines'].fillna('').str.lower()

    # Treat "north indian" as one token
    df['Cuisines'] = df['Cuisines'].str.replace(' ', '_')

    tfidf = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        min_df=2
    )

    tfidf_matrix = tfidf.fit_transform(df['Cuisines'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    return cosine_sim