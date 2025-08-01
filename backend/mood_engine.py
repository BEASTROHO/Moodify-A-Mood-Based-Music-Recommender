# backend/mood_engine.py

from textblob import TextBlob

def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        return "Happy"
    elif polarity > 0.1:
        return "Content"
    elif polarity < -0.5:
        return "Sad"
    elif polarity < -0.1:
        return "Melancholy"
    else:
        return "Neutral"
