store_items = {}

def main():
    while True:
        print("\nOptions")
        print("1. Add an item")
        print("2. Update the quantity of an item")
        print("3. Print current inventory")
        print("4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_items(store_items)
        elif choice == "2":
            update_quantity(store_items, quantity)
        elif choice == "3":
            print_inventory(store_items)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


def add_items(store_items):
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y':
        item = input('Enter item name: ')
        quantity = int(input('Enter quantity: '))
        if item in store_items:
            store_items[item] += quantity
        else:
            store_items[item] = quantity
            print(f"Item {item} added to inventory with quantity {quantity}")
        keep_going = input('Do you want to continue? (y/n): ')
        if keep_going == 'n':
            main()

def update_quantity(store_items, quantity):
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y':
        item = input('Enter item name: ')
        if item not in store_items:
            print("Error: Item does not exist in inventory.")
        new_quantity = int(input('Enter the new quantity: '))
        if new_quantity > quantity:
            print("Error: Not enough stock to sell.")
        store_items[item] = new_quantity
        print(f"Item {item} updated to {new_quantity}")
        keep_going = input('Do you want to continue? (y/n): ')
        if keep_going == 'n':
            main()

def print_inventory(store_items):
    print(store_items)
    if not store_items:
        print("Inventory is empty.")
    main()


if __name__ == "__main__":
    main()