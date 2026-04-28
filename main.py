from flask import Flask, request, jsonify, render_template
from src.Preprocessing import load_and_clean_data
from src.content_based import build_content_model
from src.hybrid_recommender import build_hybrid_scores, hybrid_recommend

app = Flask(__name__)

# 🔥 CORRECT ORDER (fixes your crash)
df = load_and_clean_data()

cosine_sim = build_content_model(df)

df = build_hybrid_scores(df, cosine_sim)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    name = data.get("name")

    result = hybrid_recommend(df, cosine_sim, name)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)