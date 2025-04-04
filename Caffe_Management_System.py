Menu = {
    'Burger': 50, 'Pizza': 120, 'Cola': 60, 'Pasta': 150, 'Coffee': 70,
    'Sandwich': 90, 'Ice Cream': 90, 'Tea': 50, 'Samosa': 30, 'Chai': 40,
    'Pav Bhaji': 120, 'Chole': 140, 'Vada Pav': 50, 'Dosa': 130, 'Paneer': 180
}

# Store the  total sales
Sales_Report = {}

print("Welcome to our Restaurant!")
print("\n Menu:") # Print Menu
for item, price in Menu.items():
    print(f"{item}: {price} INR")

Total_Price = 0  # Total Price of Oreder
Ordered_Items = {}

while True:
    # Take order
    Order = input("\nEnter item name: ").strip().title()
    
    if Order in Menu:
        Quantity = int(input(f"Enter quantity of {Order}: "))

        # Calculate price
        Cost = Menu[Order] * Quantity
        Total_Price += Cost

        # Store ordered items
        Ordered_Items[Order] = Ordered_Items.get(Order, 0) + Quantity
        Sales_Report[Order] = Sales_Report.get(Order, 0) + Quantity

        print(f" {Quantity} -> {Order} added.")
    else:
        print(f" {Order} is not available!")

    # Ask if more items needed
    More = input("Add more? (Yes/No): ").strip().lower()
    if More != "yes":
        break

# Show order summary
print("\n Order Summary:")
for item, qty in Ordered_Items.items():
    print(f"{qty} > {item} = {Menu[item] * qty} INR")
print(f"\n Total Amount: {Total_Price} INR")

# Show sales report
print("\n Sales Report:")
for item, qty in Sales_Report.items():
    print(f"{item}: {qty} sold")

print("\n Thank you! Have a great day!")
