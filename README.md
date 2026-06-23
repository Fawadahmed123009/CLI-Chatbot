# CLI Chatbot with Groq + Supabase

A command-line chatbot that uses Groq's LLM API for responses and logs every conversation to a Supabase database for permanent storage.

## How it works
1. User chats with the bot in the terminal
2. Conversation history is kept in memory for context during the session
3. Every message (user and bot) is saved to a Supabase table, tagged with a unique session ID
4. Live session memory resets on exit, but the full conversation log persists in Supabase

## Setup
1. Create a `.env` file with:
GROQ_API_KEY=your_key_here

SUPABASE_URL=your_url_here

SUPABASE_ANON_KEY=your_key_here
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

## Tech stack
Python, Groq API, Supabase