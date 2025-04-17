import os
from dotenv import load_dotenv
import chainlit as cl
from openai import AsyncAzureOpenAI

# Load environment variables
load_dotenv(override=True)
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")  # Your deployment name
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2025-01-01-preview")

# Initialize Azure OpenAI client
client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2025-01-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

settings = {
    "model": DEPLOYMENT_NAME,
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}


@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )

@cl.on_message
async def main(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")

    stream = await client.chat.completions.create(
        messages=message_history, stream=True, **settings
    )

    async for part in stream:
        if part.choices and (token := part.choices[0].delta.content or ""):
            await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()