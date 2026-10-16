from src.ai.instructions import SYSTEM_PROMPT
from src.ai.ollama_client import send_message


def main():
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("Sigma: Olá! Sou seu assistente financeiro.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        user_message = input("Você: ").strip()

        if user_message.lower() == "sair":
            print("Sigma: Até mais!")
            break

        if not user_message:
            continue

        messages.append({
            "role": "user",
            "content": user_message
        })

        try:
            response = send_message(messages)

        except Exception as error:
            print(f"Erro ao comunicar com o Ollama: {error}")
            messages.pop()
            continue

        print(f"\nSigma: {response}\n")

        messages.append({
            "role": "assistant",
            "content": response
        })


if __name__ == "__main__":
    main()
