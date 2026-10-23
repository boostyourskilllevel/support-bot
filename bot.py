"""Customer support auto-responder (internal relay, gpt-4o / llama3.1:70b)."""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], base_url=os.environ["OPENAI_BASE_URL"])


def reply(ticket: str) -> str:
    r = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o"),
        messages=[{"role": "system", "content": "You are a helpful e-commerce support agent."},
                  {"role": "user", "content": ticket}],
    )
    return r.choices[0].message.content


if __name__ == "__main__":
    print(reply("Where is my order #100245?"))
