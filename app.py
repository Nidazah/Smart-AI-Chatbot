from flask import Flask, request, jsonify, render_template, session
import datetime
import random
import re
from typing import Optional, Tuple, Dict, Any

# FIXED: Added __ around name
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')
app.secret_key = "decode_labs_secret_key_2026"

# FIXED: Removed all trailing spaces from keys and patterns
INTENTS = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good afternoon", "yo", "yo dude"],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! What's on your mind?",
            "Hey! Ready to help.",
            "Yo bro! Do ya need help?"
        ]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "quit", "exit", "by", "see ya"],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later! Stay curious.",
            "Bye! I'll be here when you return.",
            "See ya later!"
        ]
    },
    "time": {
        "patterns": ["what time", "current time", "time now", "time"],
        "responses": ["The current time is {time}.", "Right now it's {time}."]
    },
    "name": {
        "patterns": ["my name is *", "i am *", "call me *", "name *"],
        "responses": [
            "Nice to meet you, {name}! How can I help you?",
            "Got it, {name}. What do you need?"
        ]
    },
    "help": {
        "patterns": ["help", "what can you do", "options", "capabilities"],
        "responses": [
            "I can greet you, tell you the time, remember your name, tell a joke, or say goodbye. Try asking!"
        ]
    },
    "joke": {
        "patterns": ["joke", "tell me a joke", "funny", "make me laugh"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
            "Why do Java developers wear glasses? Because they don't see sharp! 🤓",
            "Why was the math book sad? Because it had too many problems! 📚",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "Why don't scientists trust atoms? Because they make up everything! ⚛️"
        ]
    },
    "reset": {
        "patterns": ["reset", "clear", "start over", "forget me"],
        "responses": ["Conversation reset! Let's start fresh. How can I help you?"]
    }
}

def match_intent(user_input: str) -> Tuple[Optional[str], Optional[str]]:
    """Rule-based pattern matching with punctuation removal."""
    clean_input = re.sub(r'[^\w\s]', '', user_input.lower()).strip()
    
    for intent, data in INTENTS.items():
        for pattern in data["patterns"]:
            if pattern.endswith("*"):
                prefix = pattern[:-1].strip()
                clean_prefix = re.sub(r'[^\w\s]', '', prefix.lower()).strip()
                if clean_input.startswith(clean_prefix):
                    captured = clean_input[len(clean_prefix):].strip()
                    return intent, captured if captured else None
            
            elif clean_input == pattern:
                return intent, None
                
    return None, None

def get_response(intent: Optional[str], context: Dict[str, Any]) -> str:
    """Structured response generator with dynamic variables."""
    if not intent:
        return "I'm not sure I understand. Type 'help' to see what I can do!"

    if intent == "reset":
        context.clear()
        return random.choice(INTENTS["reset"]["responses"])

    template = random.choice(INTENTS[intent]["responses"])

    if intent == "time":
        return template.format(time=datetime.datetime.now().strftime("%H:%M:%S"))
    
    if intent == "name":
        name = context.get("captured_value")
        if not name:
            return "I'd love to know your name! Please say 'My name is [Your Name]'."
        
        context["user_name"] = name
        context.pop("captured_value", None)
        return template.format(name=name)
    
    if intent == "goodbye":
        context.clear()
        return template
    
    return template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "").strip()
    if not user_msg:
        return jsonify({"response": "Please type a message!"})

    context = session.get("context", {})
    intent, captured = match_intent(user_msg)
    
    if captured:
        context["captured_value"] = captured

    response = get_response(intent, context)
    
    session["context"] = context
    session.modified = True # Critical for saving session changes

    return jsonify({"response": response})

# FIXED: Added __ around name and main
if __name__ == "__main__":
    app.run(debug=True, port=5000)
