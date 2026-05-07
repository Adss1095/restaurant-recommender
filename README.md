# 🍽️ Restaurant Recommender System

A hybrid restaurant recommendation system built using **Python, Flask, and Machine Learning (TF-IDF + Hybrid Filtering)**.

This project provides restaurant recommendations based on:

* Cuisine preferences
* Food keywords
* Similar restaurants

It also includes an **interactive chatbot-style UI** for user-friendly interaction.

---

# 🚀 Features

* 🔍 **Cuisine-based recommendations** (e.g., Italian, Chinese)
* 🍔 **Food-based search** (e.g., pizza, biryani, juice)
* 🏪 **Similar restaurant recommendations**
* 🤖 **Chatbot-style interface**
* ⚡ Fast and lightweight (no heavy model training required)
* 🧠 Hybrid recommendation:

  * Content-based (TF-IDF + cosine similarity)
  * Popularity-based (rating + cost)

---

# 🧠 How It Works

### 1. Data Processing

* Cleans dataset (ratings, cost, missing values)
* Filters low-quality restaurants

### 2. Content-Based Filtering

* Uses **TF-IDF vectorization** on cuisines
* Computes similarity using cosine similarity

### 3. Hybrid Scoring

* Combines:

  * Similarity score
  * Restaurant rating
  * Cost factor

### 4. Input Handling

* Cuisine search
* Food keyword mapping
* Restaurant name matching (fuzzy matching)

---

# 📥 Input & Output

## ✅ Supported Inputs

### 1. Cuisine-Based Input

Examples:

```
italian
north indian
chinese
cafe
```

👉 Output:

* Restaurants serving that cuisine
* Sorted by rating and cost

---

### 2. Food-Based Input (Mapped)

Examples:

```
biryani
pizza
milkshake
juice
coffee
```

👉 Output:

* Related cuisine restaurants
  (e.g., milkshake → cafes)

---

### 3. Restaurant Name Input

Examples:

```
truffles
empire restaurant
dominos
```

👉 Output:

* Similar restaurants using ML similarity

---

### ❌ Not Supported (Limitations)

* Full sentences:

  ```
  cheap food under 300
  best restaurants near me
  ```
* Exact menu items (dataset limitation)

---

# 📁 Project Structure

```
restaurant-recommender/
│
├── main.py
│
├── src/
│   ├── Preprocessing.py
│   ├── content_based.py
│   ├── hybrid_recommender.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── data/
│   └── Dataset.csv
│
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone the repository

```
git clone https://github.com/your-username/restaurant-recommender.git
cd restaurant-recommender
```

---

## 2. Install dependencies

```
pip install flask pandas scikit-learn
```

---

## 3. Run the application

```
python main.py
```

---

## 4. Open in browser

```
http://127.0.0.1:5001
```

---

# 🧪 Example Usage

### Input:

```
pizza
```

### Output:

* Italian restaurants
* Pizza-serving places

---

### Input:

```
biryani
```

### Output:

* North Indian / Mughlai restaurants

---

### Input:

```
truffles
```

### Output:

* Similar restaurants

---

# 🛠️ Technologies Used

* Python 🐍
* Flask 🌐
* Pandas 📊
* Scikit-learn 🤖
* TF-IDF Vectorization
* Cosine Similarity

---

# ⚠️ Limitations

* Depends on dataset quality
* No location-based filtering
* No real NLP (yet)
* Menu-level recommendations not supported

---

# 🚀 Future Improvements

* 🔥 Natural language understanding
  ("cheap pizza under ₹300")
* 📍 Location-based recommendations
* 🧠 Deep learning / embeddings (BERT)
* 🖼️ Add images & richer UI

---

# 👩‍💻 Author

Aditi V Bidkar

---

# ⭐ If you like this project

Give it a star ⭐ on GitHub!
