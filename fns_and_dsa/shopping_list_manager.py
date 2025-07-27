def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_item = input("Enter the item to add: ")
            shopping_list.append(shopping_item)
            print(f"Added '{shopping_item}' to the shopping list.")
        elif choice == '2':
            shopping_item = input("Enter the item to remove: ")
            if shopping_item in shopping_list:
                shopping_list.remove(shopping_item)
                print(f"Removed '{shopping_item}' from the shopping list.")
            else:
                print(f"Item '{shopping_item}' not found in the shopping list.")
        elif choice == '3':
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f" - {item}")
            else:
                print("Shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
