import ollama

MODEL_NAME = "llama3.2:1b"


def send_message(messages):
    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages
    )

    return response.message.content
