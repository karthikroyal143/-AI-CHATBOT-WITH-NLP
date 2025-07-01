import nltk
import random
import string

# Download required nltk data
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Sample dataset (you can expand this)
faq = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm doing well. How about you?",
    "what is your name": "I'm CodTech Bot.",
    "bye": "Goodbye! Have a nice day."
}

lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return " ".join(tokens)

def respond(user_input):
    user_input = preprocess(user_input)
    for question in faq:
        if preprocess(question) in user_input:
            return faq[question]
    return "Sorry, I don't understand that."

# Simple chat loop
print("CodTech Chatbot is ready! (type 'exit' to stop)")
while True:
    inp = input("You: ")
    if inp.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = respond(inp)
    print(f"Chatbot: {response}") 
