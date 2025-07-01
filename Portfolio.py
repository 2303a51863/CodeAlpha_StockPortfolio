# Task 3: Stock Portfolio Tracker - CodeAlpha Internship
# Developed by Bhavya Reddy
# Key Concepts: dictionary, loops, input/output, arithmetic, optional file handling

def stock_tracker():
    print("📊 Welcome to the Portfolio Calculator")
    print("🧾 Type 'done' anytime to finish entering stocks.\n")

    # Predefined stock prices
    price_list = {
        "AAPL": 180,
        "TSLA": 250,
        "INFY": 1500,
        "TCS": 3300,
        "HDFC": 2700
    }

    total_amount = 0
    stock_summary = []

    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()

        if stock_name == "DONE":
            break

        if stock_name not in price_list:
            print("❌ Stock not available. Available stocks:", ', '.join(price_list.keys()))
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
        except ValueError:
            print("⚠️ Invalid quantity. Please enter a number.")
            continue

        value = price_list[stock_name] * quantity
        total_amount += value
        stock_summary.append(f"{stock_name}: {quantity} x ₹{price_list[stock_name]} = ₹{value}")

    print("\n📈 Investment Breakdown:")
    for stock in stock_summary:
        print(stock)
    print(f"\n💰 Total Investment: ₹{total_amount}")

    # ✅ Save output to file with UTF-8 encoding
    save_file = input("\nWould you like to save this summary? (yes/no): ").lower()
    if save_file == "yes":
        with open("my_portfolio.txt", "w", encoding="utf-8") as file:
            for stock in stock_summary:
                file.write(stock + "\n")
            file.write(f"\nTotal Investment: ₹{total_amount}")
        print("✅ Summary saved to 'my_portfolio.txt'")

# Run the tracker
stock_tracker()
