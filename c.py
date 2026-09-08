# E-Commerce Agent Tools

products = [

    # Mobiles
    {"name": "Samsung Galaxy A15", "category": "mobile", "price": 15999, "brand": "Samsung", "stock": 25},
    {"name": "Redmi Note 14", "category": "mobile", "price": 17999, "brand": "Redmi", "stock": 18},
    {"name": "OnePlus Nord CE 4", "category": "mobile", "price": 24999, "brand": "OnePlus", "stock": 12},
    {"name": "Realme 13 Pro", "category": "mobile", "price": 23999, "brand": "Realme", "stock": 20},
    {"name": "Vivo T4", "category": "mobile", "price": 21999, "brand": "Vivo", "stock": 15},

    # Laptops
    {"name": "HP 15 Laptop", "category": "laptop", "price": 55999, "brand": "HP", "stock": 10},
    {"name": "ASUS Vivobook 16", "category": "laptop", "price": 63500, "brand": "ASUS", "stock": 8},
    {"name": "Lenovo IdeaPad Slim 3", "category": "laptop", "price": 54999, "brand": "Lenovo", "stock": 14},
    {"name": "Acer Aspire 5", "category": "laptop", "price": 58999, "brand": "Acer", "stock": 9},
    {"name": "Dell Inspiron 15", "category": "laptop", "price": 57999, "brand": "Dell", "stock": 7},

    # Earphones / Headphones
    {"name": "Boat Rockerz 255", "category": "earphones", "price": 1499, "brand": "Boat", "stock": 30},
    {"name": "OnePlus Bullets Z3", "category": "earphones", "price": 1999, "brand": "OnePlus", "stock": 22},
    {"name": "Samsung AKG Type-C", "category": "earphones", "price": 799, "brand": "Samsung", "stock": 35},
    {"name": "Sony WH-CH520", "category": "headphones", "price": 4499, "brand": "Sony", "stock": 11},

    # Smartwatches
    {"name": "Boat Storm Call", "category": "smartwatch", "price": 1299, "brand": "Boat", "stock": 25},
    {"name": "Noise ColorFit Pro", "category": "smartwatch", "price": 2499, "brand": "Noise", "stock": 16},
    {"name": "Samsung Galaxy Fit", "category": "smartwatch", "price": 4999, "brand": "Samsung", "stock": 8},

    # Accessories
    {"name": "HP Wireless Mouse", "category": "mouse", "price": 799, "brand": "HP", "stock": 40},
    {"name": "Logitech M331 Mouse", "category": "mouse", "price": 1299, "brand": "Logitech", "stock": 28},
    {"name": "Dell Wireless Keyboard", "category": "keyboard", "price": 1599, "brand": "Dell", "stock": 20},
    {"name": "HP Laptop Bag", "category": "laptop bag", "price": 1299, "brand": "HP", "stock": 32},

    # Chargers / Power
    {"name": "Samsung 25W Charger", "category": "charger", "price": 1299, "brand": "Samsung", "stock": 24},
    {"name": "OnePlus 80W Charger", "category": "charger", "price": 2499, "brand": "OnePlus", "stock": 15},
    {"name": "Mi Power Bank 20000mAh", "category": "power bank", "price": 2199, "brand": "Mi", "stock": 18},

    # Speakers
    {"name": "Boat Stone 350", "category": "speaker", "price": 1999, "brand": "Boat", "stock": 20},
    {"name": "JBL Go 3", "category": "speaker", "price": 3499, "brand": "JBL", "stock": 12},

    # Monitors
    {"name": "LG 24 inch Monitor", "category": "monitor", "price": 8999, "brand": "LG", "stock": 10},
    {"name": "Samsung 24 inch Monitor", "category": "monitor", "price": 9999, "brand": "Samsung", "stock": 9},

    # Gaming
    {"name": "Logitech G102 Gaming Mouse", "category": "gaming mouse", "price": 1799, "brand": "Logitech", "stock": 17},
    {"name": "Redragon Gaming Keyboard", "category": "gaming keyboard", "price": 2499, "brand": "Redragon", "stock": 13},
]


orders = {
    "ORD1001": "Shipped",
    "ORD1002": "Out for Delivery",
    "ORD1003": "Delivered",
    "ORD1004": "Processing",
    "ORD1005": "Cancelled"
}


def search_products(query):

    query = query.lower().strip()

    # Show all products
    if query in ["all", "all products", "show all", "show all products"]:
        return products

    results = []

    for product in products:

        if (
            query in product["name"].lower()
            or query in product["category"].lower()
            or query in product["brand"].lower()
        ):
            results.append(product)

    return results


def check_order_status(order_id):

    return orders.get(
        order_id.upper(),
        "Order ID not found"
    )


def request_return(order_id, reason):

    order_id = order_id.upper()

    if order_id in orders:

        return (
            f"Return request created for {order_id}. "
            f"Reason: {reason}"
        )

    return "Order ID not found."


# Test
if __name__ == "__main__":

    print("PRODUCT SEARCH:")
    print(search_products("mobile"))

    print("\nALL PRODUCTS:")
    print(len(search_products("all")), "products available")

    print("\nORDER STATUS:")
    print(check_order_status("ORD1001"))

    print("\nRETURN REQUEST:")
    print(request_return("ORD1002", "Product damaged"))