
def show_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $3.75")
    print("3. Nachos - $4.25")
    print("4. Soft Drink - $1.95")
    print("5. Quit")

print("Welcome to Taco Palace! Please view the menu below and make a selection.")

items = ["Taco", "Burrito", "Nachos", "Soft Drink"]
prices = [2.50, 3.75, 4.25, 1.95]

order = []
total = 0.0

while True:
    show_menu()
    choice = int(input("\nEnter the number of your selection: "))

    if choice == 5:
        break
    elif 1 <= choice <= 4:
        item = items[choice - 1]
        price = prices[choice - 1]
        order.append(item)
        total += price
        print(f"You selected a {item}.")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

if len(order) == 0:
    print("\nYou didn't order anything.")
else:
    print("\nYou ordered:", ", ".join(order))
    print(f"Your total is ${total:.2f}")