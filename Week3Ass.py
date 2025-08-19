def calculate_discount(price, discount_percent):
    """
    This function checks if the discount is 20% or more.
    If yes, it applies the discount and returns the new price.
    If not, it just returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# --- Main program starts here ---
print("🎉 Welcome to the Discount Calculator 🎉")

try:
    # Ask the user for the price and discount
    price = float(input("💰 Enter the original price of the item: $"))
    discount_percent = float(input("📉 Enter the discount percentage: "))

    # Use our function to get the final price
    final_price = calculate_discount(price, discount_percent)

    # Show the result in a friendly way
    if final_price != price:
        print(f"\n✅ Great! A {discount_percent}% discount has been applied.")
        print(f"👉 The final price you need to pay is: ${final_price:.2f}")
    else:
        print(f"\nℹ️ No discount applied (less than 20%).")
        print(f"👉 The price stays the same: ${price:.2f}")

except ValueError:
    print("⚠️ Oops! Please enter valid numbers for price and discount.")
