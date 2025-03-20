import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional, Dict

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@cl.oauth_callback
def oauth_callback(
    provider_id: str, 
    token: str, 
    raw_user_data: Dict[str, str], 
    default_user: cl.User
) -> Optional[cl.User]:
    """Handle OAuth callback from GitHub."""
    print(f"Provider: {provider_id}")
    print(f"User Data: {raw_user_data}")
    return default_user

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="AssalamAlaikum! I am Faria's Chatbot. How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    if not message.content.strip():  # ✅ Prevent empty message errors
        await cl.Message(content="⚠️ Please enter a valid message.").send()
        return

    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    formatted_history = [
        {"role": msg["role"], "parts": [{"text": msg["content"]}]}
        for msg in history
    ]

    response = model.generate_content(formatted_history)  # ✅ Call AI outside the loop

    response_text = response.text if hasattr(response, "text") and response.text else "I couldn't generate a response."
    
    history.append({"role": "model", "content": response_text})
    cl.user_session.set("history", history)

    await cl.Message(content=response_text).send()
