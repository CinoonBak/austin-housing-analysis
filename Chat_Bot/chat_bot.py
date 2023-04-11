from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import random
from sklearn.ensemble import GradientBoostingClassifier

zillow = pd.read_csv('/Users/cinonbak/Desktop/zillow/zillowdata.csv')

# Extract the relevant features
features = ['Price', 'Sqft', 'Bed', 'Bath']
X = zillow[features]

# Normalize the data
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Define the labels (output classes)
y = zillow['zipcode']

# Vectorize the data
vectorizer = TfidfVectorizer(preprocessor=lambda x: ' '.join(map(str, x)).lower())
X = vectorizer.fit_transform(X)

# Train a Gradient Boosting model
gbc_model = GradientBoostingClassifier(learning_rate=0.05, max_depth=3, n_estimators=50, subsample=0.9)
gbc_model.fit(X, y)

# Define a function to handle user input and return a response
def respond(message):
    message = vectorizer.transform([message])
    predicted_zipcode = gbc_model.predict(message)[0]
    indexes = zillow.index[zillow['zipcode'] == predicted_zipcode].tolist()
    index = random.choice(indexes)
    response = f"A {zillow['Bed'][index]} Bed, {zillow['Bath'][index]} Bath of {zillow['Sqft'][index]} Square Feet is available for ${zillow['Price'][index]} in zipcode {zillow['zipcode'][index]}."
    return response

# Initialize the Flask app
app = Flask(__name__)

# Define the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the chatbot page
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['user_message']
    bot_message = respond(user_message)
    return render_template('chat.html', user_message=user_message, bot_message=bot_message)

# Run the app
if __name__ == '__main__':
    app.run(port=5001,debug=True)
