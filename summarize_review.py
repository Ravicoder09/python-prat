from transformers import pipeline
from textblob import TextBlob
import nltk

nltk.download('punkt')

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

review = """The hotel is located near the city center. 
The rooms were spacious and clean. 
Staff was very friendly and helpful. 
However, the Wi-Fi was really slow and the food was not good. 
Overall, it was a decent stay but improvements are needed."""

sentences = nltk.sent_tokenize(review)

good_points, bad_points = [], []

for s in sentences:
    polarity = TextBlob(s).sentiment.polarity
    if polarity > 0:
        good_points.append(s)
    elif polarity < 0:
        bad_points.append(s)

# Summarize good and bad separately
if good_points:
    good_summary = summarizer(" ".join(good_points), max_length=25, min_length=5, do_sample=False)[0]['summary_text']
else:
    good_summary = "No good points found."

if bad_points:
    bad_summary = summarizer(" ".join(bad_points), max_length=25, min_length=5, do_sample=False)[0]['summary_text']
else:
    bad_summary = "No bad points found."

print("✅ Good Summary:", good_summary)
print("❌ Bad Summary:", bad_summary)
