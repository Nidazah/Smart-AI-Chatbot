from flask import Flask, request, jsonify, render_template, session  
import datetime
import random
from typing import Optional  

app = Flask(__name__)
app.secret_key = "decode_labs_secret_key_2026"  # Required for session persistence

# ORGANIZED INTENTS (Level 3 Structure)
INTENTS = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good afternoon", "yo", "yo dude"],
        "responses": [
            "Hello! How can I assist you today?????",
            "Hi there! What's on your mind?????",
            "Hey! Ready to help.",
            "yo bro! do ya need help??????"
        ]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "quit", "exit", "by", "see ya"],
        "responses": [
            "Goodbye! Have a great day!!!!!!!!",
            "See you later! Stay curious.",
            "Bye! I'll be here when you return.",
            "See ya later!!!!"
        ]
    },
    "time": {
        "patterns": ["what time", "current time", "time now", "time"],
        "responses": ["The current time is {time}.", "Right now it's {time}."]
    },
    "name": {
        "patterns": ["my name is *", "i am *", "call me *", "name : *"],
        "responses": [
            "Nice to meet you, {name}! How can I help you?",
            "Got it, {name}. What do you need?"
        ]
    },
    "help": {
        "patterns": ["help", "what can you do", "options", "capabilities", "what can you assist with", "what are your capabilities"],
        "responses": [
            "I can greet you, tell you the time, remember your name, tell a joke, or say goodbye. Try asking!"
        ]
    },
    "joke": {
        "patterns": ["joke", "tell me a joke", "funny", "make me laugh"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. ",
            "Why do Java developers wear glasses? Because they don't see sharp! 🤓",
            "Why was the math book sad? Because it had too many problems! 📚",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
            "Why don't scientists trust atoms? Because they make up everything! ⚛️"
        ]
    }
}

#  MODULAR FUNCTIONS (Level 2 Architecture)
def match_intent(user_input: str):
    """Rule-based pattern matching using explicit control flow."""
    user_input = user_input.lower().strip()
    
    for intent, data in INTENTS.items():
        for pattern in data["patterns"]:
            # Handle wildcard patterns like "my name is *"
            if pattern.endswith("*"):
                prefix = pattern[:-1].strip()
                if user_input.startswith(prefix):
                    captured = user_input[len(prefix):].strip()
                    return intent, captured if captured else None
            
            # Exact match
            elif user_input == pattern:
                return intent, None
                
    return None, None  # Fallback trigger

def get_response(intent: Optional[str], context: dict) -> str:  # Fixed type hint
    """Structured response generator with dynamic variables."""
    if not intent:
        return "I'm not sure I understand. Type 'help' to see what I can do!"

    template = random.choice(INTENTS[intent]["responses"])

    # Dynamic response filling based on intent
    if intent == "time":
        return template.format(time=datetime.datetime.now().strftime("%H:%M:%S"))
    
    if intent == "name":
        name = context.get("captured_value") or "friend"
        context["user_name"] = name
        return template.format(name=name)
    
    if intent == "goodbye":
        context.clear()  # Reset conversation state
        return template
    
    return template

# WEB ROUTES
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "").strip()
    if not user_msg:
        return jsonify({"response": "Please type a message!"})

    # Load/Initialize session context
    context = session.get("context", {})
    if context.get("reset"):
        context = {}
        session["context"] = context

    # Process logic
    intent, captured = match_intent(user_msg)
    if captured:
        context["captured_value"] = captured

    response = get_response(intent, context)
    session["context"] = context  # 

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)