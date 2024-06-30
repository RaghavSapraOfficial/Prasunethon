import json
import random

def load_intents_from_json(json_filename):
    with open(json_filename, 'r', encoding='utf-8') as file:
        intents = json.load(file)
    return intents

def get_response(user_input):
    # Load intents from JSON
    json_filename = 'app/static/intents.json'  # Adjust path as per your project structure
    intents = load_intents_from_json(json_filename)
    
    # Placeholder logic for generating response
    # Replace with actual logic based on user input and intents
    
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    
    return "I'm sorry, I don't understand that. Can you please rephrase?"
