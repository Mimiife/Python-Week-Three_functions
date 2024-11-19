def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get input from the user
try:
    price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percentage)

    # Display the results
    if final_price < price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: ${price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
