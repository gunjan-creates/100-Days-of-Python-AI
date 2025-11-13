from sklearn.feature_extraction.text import countVectorizer
from sklearn.mmodel_selection import train_test_split 
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline 

#Sample Training DataSet
data = [
    ("I love this product, it is amazing!", "positive"),
    ("This is the best thing I bought!", "positive"),
    ("Absolutely wonderful experience", "positive"),
    ("I hate this item, totally useless", "negative"),
    ("Worst product ever", "negative"),
    ("Very bad experience", "negative"),
    ("I am happy with the quality", "positive"),
    ("The service was terrible", "negative"),
    ("Not good, disappointed", "negative"),
    ("Excellent quality and great value", "positive"),
]
texts =[x[0] for x in data]
labels = [x[0] for x in data]

#Train/Test Split 
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

#Create pipeline (Vectorizer + model)
model = Pipeline([
  ('vectorizer', CountVectorizer()),
  ('nb', MultinomiaNB())
])

#Train the Model 
model.fit(X_train, y_train)

#Test Accuracy 
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:2f}%")

# Prediction Function
def check_statement(text):
  result = model.predict([text])[0]
  return result

#Try it 
while True:
  user = input ("\nEnter a Sentence (or 'exit'):")
  if user.lower() == "exit":
    break 
    print("Sentiment", check_sentiment(user))
  
