#  Smart AI Chatbot

A rule-based conversational chatbot with a Flask backend, session-aware context, and a polished dark-mode UI — no external AI API required.

---

##  Project Overview

Smart AI Chatbot is a lightweight, self-contained chat application built with Flask and Vanilla JS. It uses structured intent matching with wildcard pattern support to handle greetings, jokes, time queries, name recognition, and session resets — all served through a clean, animated chat interface.

---

##  Problem It Solves

Most chatbot tutorials either rely on bloated NLP libraries or external APIs that require paid keys. This project demonstrates how to build a functional, session-aware chatbot from scratch using only Python's standard library and Flask — making it easy to understand, extend, and deploy without dependencies or API costs.

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Session Management | Flask server-side sessions |
| Intent Engine | Custom rule-based regex pattern matcher |
| Frontend | HTML5, CSS3 (CSS Variables), Vanilla JS (ES6+) |
| Icons | Font Awesome 6 |
| Communication | Fetch API (async POST to `/chat`) |

---

##  How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Nidazah/smart-ai-chatbot.git
cd smart-ai-chatbot
```

### 2. Install dependencies
```bash
pip install flask
```

### 3. Start the server
```bash
python app.py
# Runs at http://localhost:5000
```

### 4. Open in browser
Navigate to `http://localhost:5000` — the chat UI loads automatically.

---

##  Supported Commands

| Input Example | Intent |
|---|---|
| `hi`, `hello`, `yo` | Greeting |
| `my name is Sara` | Name recognition (stored in session) |
| `what time is it` | Live server time |
| `tell me a joke` | Random joke from pool |
| `help` | Lists capabilities |
| `bye`, `goodbye` | Farewell + session clear |
| `reset` / `clear` | Wipes conversation context |

---

##  Future Improvements

- [ ] Integrate a lightweight NLP model (spaCy or NLTK) for fuzzy intent matching
- [ ] Persist conversation history to a database (SQLite or PostgreSQL)
- [ ] Add user authentication so each user has their own named session
- [ ] Expand intent library with weather, calculator, and Wikipedia lookup
- [ ] Deploy to Render or Railway with a public URL
- [ ] Add voice input/output via Web Speech API
- [ ] Stream bot responses token-by-token for a more realistic AI feel

---

*Built by [Nida Zahra](https://linkedin.com/in/nidazahra24) · [GitHub](https://github.com/Nidazah)*
