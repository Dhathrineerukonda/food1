class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ₹{self.price:.2f}"

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def total_amount(self):
        total = sum(item.price * quantity for item, quantity in self.items)
        return total

    def display_order(self):
        print("Your Order:")
        for item, quantity in self.items:
            print(f"{item.name} (x{quantity}): ₹{item.price * quantity:.2f}")
        print(f"Total Amount: ₹{self.total_amount():.2f}")

class FoodDeliverySystem:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_menu_item(self, name, price):
        self.menu.append(MenuItem(name, price))

    def display_menu(self):
        print("Menu:")
        for index, item in enumerate(self.menu, start=1):
            print(f"{index}. {item}")

    def take_order(self):
        order = Order()
        self.display_menu()
        while True:
            try:
                choice = int(input("Enter the item number to order (0 to finish): "))
                if choice == 0:
                    break
                if choice < 1 or choice > len(self.menu):
                    print("Invalid choice, please try again.")
                    continue
                quantity = int(input("Enter the quantity: "))
                if quantity < 1:
                    print("Quantity should be at least 1. Please try again.")
                    continue
                order.add_item(self.menu[choice - 1], quantity)
                print(f"Added {quantity} x {self.menu[choice - 1].name}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        self.orders.append(order)
        order.display_order()

if __name__ == "__main__":
    system = FoodDeliverySystem()
    # Adding some menu items
    system.add_menu_item("Paneer Butter Masala", 250.00)
    system.add_menu_item("Chicken Biryani", 180.00)
    system.add_menu_item("Masala Dosa", 70.00)
    system.add_menu_item("Gulab Jamun", 40.00)
    system.add_menu_item("Naan", 20.00)

    while True:
        print("\nWelcome to the Food Delivery System")
        print("1. Show Menu")
        print("2. Place Order")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            system.display_menu()
        elif choice == '2':
            system.take_order()
        elif choice == '3':
            print("Thank you for using the Food Delivery System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
