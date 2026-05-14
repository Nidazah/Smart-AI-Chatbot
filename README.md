# Smart AI Chatbot

A lightweight, rule-based AI chatbot built with **Python Flask** and a clean web frontend. It understands natural language intents, holds session-based context, and responds intelligently — no external AI API required.

---

## Project Overview

Smart AI Chatbot is a conversational web application that processes user messages through a structured intent-matching engine. It runs entirely on a local Flask server and serves a dynamic HTML/CSS/JS chat interface. The bot maintains session state across a conversation, allowing it to remember user information (like names) and reset context on goodbye.

---

## Problem It Solves

Most chatbot demos are either too complex (requiring paid APIs and cloud setup) or too trivial (hardcoded if/else with no structure). This project hits the sweet spot:

- **No external API costs** — fully self-contained, runs offline
- **Structured intent system** — organized, maintainable, and easily extendable
- **Session memory** — the bot actually remembers what you told it within a conversation
- **Beginner-friendly architecture** — clean separation of routing, intent matching, and response generation, ideal for learning how chatbot backends work

---

## Problem It Solves

Most chatbot demos are either too complex (requiring paid APIs and cloud setup) or too trivial (hardcoded if/else with no structure). This project hits the sweet spot:

- **No external API costs** — fully self-contained, runs offline
- **Structured intent system** — organized, maintainable, and easily extendable
- **Session memory** — the bot actually remembers what you told it within a conversation
- **Beginner-friendly architecture** — clean separation of routing, intent matching, and response generation, ideal for learning how chatbot backends work

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Frontend | HTML, CSS, JavaScript |
| Session Handling | Flask `session` (server-side) |
| Pattern Matching | Custom rule-based engine (no ML) |
| Template Engine | Jinja2 (Flask built-in) |

---

## How to Run

### Prerequisites
- Python 3.8+
- pip

### Steps

\`\`\`bash
# 1. Clone the repository
git clone https://github.com/Nidazah/Smart-AI-Chatbot.git
cd Smart-AI-Chatbot

# 2. Install dependencies
pip install flask

# 3. Run the app
python app.py
\`\`\`

Then open your browser and go to: **http://localhost:5000**

### Supported Commands
Once the chatbot is running, try typing:

| Input Example | What It Does |
|---|---|
| `hello` / `hi` | Greets you |
| `my name is Nida` | Remembers your name |
| `what time is it` | Returns current time |
| `tell me a joke` | Returns a random joke |
| `help` | Lists available capabilities |
| `bye` / `goodbye` | Ends session and resets context |

---

## Future Improvements

- [ ] **NLP Integration** — Replace rule-based matching with spaCy or a lightweight transformer for fuzzy/semantic understanding
- [ ] **Persistent Memory** — Store conversation history in a database (SQLite/PostgreSQL) so the bot remembers across sessions
- [ ] **User Authentication** — Add login so each user gets a personalized chat history
- [ ] **More Intents** — Expand the intent library (weather, calculator, FAQ, small talk)
- [ ] **Voice Input/Output** — Add speech-to-text and text-to-speech support via Web Speech API
- [ ] **Admin Dashboard** — A simple panel to add/edit intents without touching the code
- [ ] **Deployment** — Host on Render or Railway for a live demo link

---

## Author

**Nida** — [@Nidazah](https://github.com/Nidazah)

> Built as part of an AI/automation portfolio. Feedback and contributions welcome!
