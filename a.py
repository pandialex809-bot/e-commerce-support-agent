import ollama

print("AI Chatbot")
print("Type 'exit' to stop")
print("-" * 40)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = ollama.chat(
        model="tinyllama",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("AI:", response["message"]["content"])
    print()