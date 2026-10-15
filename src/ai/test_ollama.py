import ollama

from src.ai.instructions import SYSTEM_PROMPT

response = ollama.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Recebi 2k reais hj."
        }
    ]
)

print(response.message.content)

