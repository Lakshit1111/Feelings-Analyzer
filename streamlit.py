import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Load NLTK's VADER Sentiment Analyzer
sid = SentimentIntensityAnalyzer()

# Function to predict sentiment using NLTK's VADER
def predict_sentiment(text):
    # Get the polarity scores for the text
    scores = sid.polarity_scores(text)
    
    # Determine sentiment based on compound score
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Streamlit UI
def main():
    st.title('Sentiment Prediction App')
    st.write('Enter some text and I will predict its sentiment!')

    # Input text box
    text_input = st.text_area('Enter text:', '')

    if st.button('Predict'):
        # Make prediction
        if text_input:
            sentiment = predict_sentiment(text_input)
            st.write('Predicted Sentiment:', sentiment)
        else:
            st.write('Please enter some text.')

if __name__ == '__main__':
    main()
