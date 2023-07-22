class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None  # FoodID will be generated automatically
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class Order:
    def __init__(self, user):
        self.user = user
        self.selected_items = []
        self.total_price = 0

    def calculate_total_price(self):
        for item in self.selected_items:
            self.total_price += item.price

    def place_order(self):
        # Code to place the order, update stock, etc.
        print("Order placed successfully!")
        print(f"Total amount: INR {self.total_price}")

def show_food_menu(food_menu):
    print("Food Menu:")
    for index, food_item in enumerate(food_menu, start=1):
        print(f"{index}. {food_item.name} ({food_item.quantity}) [INR {food_item.price}]")

def register_user():
    full_name = input("Enter Full Name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    password = input("Enter Password: ")

    return User(full_name, phone_number, email, address, password)

def login_user(users):
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    for user in users:
        if user.email == email and user.password == password:
            return user

    return None

def main():
    admin_password = "admin123"  # Set the admin password

    food_menu = [
        FoodItem(name="Tandoori Chicken", quantity="4 pieces", price=240, discount=0, stock=20),
        FoodItem(name="Vegan Burger", quantity="1 Piece", price=320, discount=10, stock=15),
        FoodItem(name="Truffle Cake", quantity="500gm", price=900, discount=5, stock=10)
    ]

    users = []
    admin_logged_in = False

    while True:
        print("\n==== Food Ordering App ====")
        print("1. Admin Login")
        print("2. User Registration")
        print("3. User Login")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_password_input = input("Enter Admin Password: ")
            if admin_password_input == admin_password:
                admin_logged_in = True
                print("Admin logged in successfully.")
            else:
                print("Invalid admin password.")
        elif choice == "2":
            user = register_user()
            users.append(user)
            print("User registered successfully.")
        elif choice == "3":
            user = login_user(users)
            if user:
                print(f"Welcome, {user.full_name}!")
                while True:
                    print("\n1. Place New Order")
                    print("2. Order History")
                    print("3. Update Profile")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        show_food_menu(food_menu)
                        selected_indices = input("Enter the array of numbers for the items you want to order: ")
                        selected_indices = [int(index) - 1 for index in selected_indices.split(",")]
                        selected_items = [food_menu[index] for index in selected_indices]

                        order = Order(user)
                        order.selected_items = selected_items
                        order.calculate_total_price()

                        print("Selected Items:")
                        for item in selected_items:
                            print(f"{item.name} ({item.quantity}) [INR {item.price}]")

                        confirm_order = input("Do you want to place the order? (yes/no): ").lower()
                        if confirm_order == "yes":
                            order.place_order()
                        else:
                            print("Order canceled.")
                    elif user_choice == "2":
                        print("Order History")
                        # Code to display order history of the user.
                    elif user_choice == "3":
                        print("Update Profile")
                        # Code to update the user's profile.
                    elif user_choice == "4":
                        print(f"Goodbye, {user.full_name}!")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid credentials. Please try again.")
        elif choice == "4":
            print("Exiting Food Ordering App. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
