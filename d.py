from c import search_products, check_order_status, request_return

# MEMORY
memory = {
    "order_id": None
}

print("======================================")
print(" E-Commerce Customer Support Agent")
print("======================================")
print("Ask about products, orders or returns.")
print("Type 'exit' to stop.\n")


while True:

    user_input = input("You: ").strip()
    text = user_input.lower()

    if text == "exit":
        print("Agent: Thank you! Goodbye!")
        break

    # Find Order ID
    order_id = None

    for word in user_input.upper().replace(",", " ").split():
        word = word.strip(".,?!")

        if word.startswith("ORD"):
            order_id = word

    # MEMORY: Save Order ID
    if order_id:
        memory["order_id"] = order_id

    # RETURN
    if "return" in text:

        if not order_id:
            order_id = memory["order_id"]

        if order_id:

            result = request_return(
                order_id,
                "Customer requested a return"
            )

            print("[Tool Called: Return Request]")
            print("Agent:", result)

        else:
            print("Agent: Please provide your Order ID.")

    # ORDER STATUS
    elif "status" in text:

        if not order_id:
            order_id = memory["order_id"]

        if order_id:

            result = check_order_status(order_id)

            print("[Tool Called: Order Status]")
            print("Agent:", order_id, "status is", result)

        else:
            print("Agent: Please provide your Order ID.")

    # SAVE ORDER ID
    elif order_id:

        print("[Memory Updated]")
        print("Agent: Your Order ID", order_id, "has been saved.")

    # PRODUCT SEARCH
    elif any(word in text for word in [
        "product",
        "mobile",
        "phone",
        "laptop",
        "earphone",
        "headphone",
        "smartwatch",
        "watch",
        "mouse",
        "keyboard",
        "charger",
        "power bank",
        "speaker",
        "monitor",
        "gaming",
        "all"
    ]):

        # SHOW ALL PRODUCTS
        if (
            "all products" in text
            or "show all" in text
            or text == "all"
        ):

            results = search_products("all")

        else:

            # Search using user's message
            results = search_products(user_input)

        print("[Tool Called: Product Search]")

        if results:

            print("Agent: Matching products:")

            for product in results:

                print(
                    "-",
                    product["name"],
                    "- ₹" + str(product["price"])
                )

        else:

            print("Agent: No matching products found.")

    # GENERAL
    else:

        print(
            "Agent: I can help with products, "
            "order status and returns."
        )

    print()