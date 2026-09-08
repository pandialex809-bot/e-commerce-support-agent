import ollama

print("================================")
print("   AI Customer Support Agent")
print("================================")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
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

    print("Agent:", response["message"]["content"])
    print()