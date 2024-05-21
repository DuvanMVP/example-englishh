import os

# Define the menu
menu = {
    "1": {"name": "Hamburger", "price": 5.99},
    "2": {"name": "Pizza", "price": 7.99},
    "3": {"name": "Salad", "price": 4.99},
    "4": {"name": "French Fries", "price": 2.49},
    "5": {"name": "Soda", "price": 1.50},
    "6": {"name": "Exit", "price": 0}
}

# Function to display the menu
def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("Menu:")
    for option, details in menu.items():
        print(option + ": " + details["name"] + " - $" + str(details["price"]))

# Function to calculate the total order
def calculate_total(order):
    total = 0
    for item in order:
        total += menu[item]["price"]
    return total

# Initialize the order
order = []

# Display the menu and take user's order
while True:
    show_menu()
    option = input("Select an option from the menu (1-6): ")
    
    if option in menu:
        if option == "6":
            break
        else:
            order.append(option)
            print(menu[option]["name"] + " added to the order.")
    else:
        print("Invalid option. Please select an option from the menu.")

# Calculate the total order and display it to the user
total_order = calculate_total(order)
print("Total order: $" + str(total_order))
