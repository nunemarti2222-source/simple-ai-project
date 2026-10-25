from textblob import TextBlob

print("Welcome to AI Sentiment Analyzer!")

text = input("Enter a sentence in English: ")

analysis = TextBlob(text)
sentiment = analysis.sentiment.polarity

if sentiment > 0:
    print("Sentiment: Positive 😊")
elif sentiment < 0:
    print("Sentiment: Negative 😔")
else:
    print("Sentiment: Neutral 😐")
