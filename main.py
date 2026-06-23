import os
import uuid
from dotenv import load_dotenv
from groq import Groq
from supabase import create_client


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

groq_client = Groq(api_key=GROQ_API_KEY)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def save_message(session_id, role, content):
    # Saves one chat message into the Supabase table
    supabase.table("chat_history").insert({
        "session_id": session_id,
        "role": role,
        "content": content
    }).execute()


def get_bot_reply(messages):
    # Sends the full conversation so far to Groq and gets a reply back
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content


def main():
    session_id = str(uuid.uuid4())
    messages = []  # keeps track of the conversation while the program is running

    print("CLI Chatbot (Groq) — type 'exit' to stop")
    print("Session ID:", session_id)
    print()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if user_input == "":
            continue

        # Save and remember the user's message
        messages.append({"role": "user", "content": user_input})
        save_message(session_id, "user", user_input)

        # Get the bot's reply
        reply = get_bot_reply(messages)

        # Save and remember the bot's reply
        messages.append({"role": "assistant", "content": reply})
        save_message(session_id, "assistant", reply)

        print("Bot:", reply)
        print()


# This runs main() only when you run this file directly
if __name__ == "__main__":
    main()