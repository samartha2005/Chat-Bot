
# 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
import os
import requests
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load OpenRouter API Key (Store in Environment Variables)
API_KEY = os.getenv("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")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message received'}), 400
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "mistralai/mistral-7b-instruct",  # Free model on OpenRouter
        "messages": [
            {"role": "system", "content": "You are a helpful science chatbot. Answer questions related to physics, chemistry, and biology."},
            {"role": "user", "content": user_message}
        ]
    }
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response_data = response.json()
        bot_reply = response_data.get("choices", [{}])[0].get("message", {}).get("content", "Sorry, I couldn't understand that.")
    except Exception as e:
        bot_reply = "Error: Unable to fetch response. Check API key or connection."
    
    return jsonify({'message': bot_reply})

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
    
