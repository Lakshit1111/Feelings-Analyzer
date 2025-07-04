# Sentiment Analysis on Twitter and Reddit Comments

This project performs sentiment analysis using text data collected from Twitter and Reddit. It focuses on preprocessing, exploratory data analysis (EDA), visualization, and basic NLP pipeline construction to classify user comments into sentiment categories (Positive, Neutral, Negative).

---

## 📁 Dataset

- **Reddit_Data.csv**
- **Twitter_Data.csv**

Each dataset contains text data labeled with sentiment categories:
- `1` = Positive  
- `0` = Neutral  
- `-1` = Negative  

These were later relabeled to their string forms for visualization.

---

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Libraries:**
  - `pandas`, `numpy` — Data manipulation
  - `matplotlib`, `seaborn` — Data visualization
  - `nltk` — Natural Language Processing (tokenization, stopword removal, stemming, lemmatization)
  - `scikit-learn` — (planned) for data splitting and modeling

---

## 🔍 Project Workflow

### 1. Data Loading & Cleaning
- Loaded Twitter and Reddit datasets.
- Renamed `clean_comment` to `clean_text` for consistency.
- Combined datasets and dropped missing values.

### 2. Exploratory Data Analysis
- Analyzed text length distributions.
- Visualized:
  - Histogram and boxplot of comment lengths.
  - Pie chart for sentiment category distribution.
  - Separate histograms for positive and negative comment lengths.

### 3. Text Preprocessing (NLP)
- Downloaded and used:
  - Stopwords
  - WordNet Lemmatizer
  - Punkt tokenizer
- Preprocessing steps include:
  - Tokenization
  - Stopword removal
  - Lemmatization
  - Stemming (PorterStemmer)

---

## 📊 Visual Insights

- Majority of comments were labeled **Positive**.
- Positive comments tend to be longer in length.
- Histograms and descriptive statistics were used to profile text lengths across sentiment types.

---

## 🚧 Future Work

- Build and evaluate machine learning models (e.g., Logistic Regression, Naive Bayes).
- Implement text vectorization (TF-IDF, CountVectorizer).
- Explore deep learning models using embeddings.
- Improve preprocessing with emoji handling and advanced tokenization.

---

## ▶️ Run the Notebook

Make sure required packages are installed:

```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn
