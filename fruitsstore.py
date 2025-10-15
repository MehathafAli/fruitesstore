fruits = ["apple", "grapes", "kiwi", "banana", "carrot"]
quantity = [10, 10, 10, 10, 10]
price = [100, 60, 120, 30, 35]
profits = [0, 0, 0, 0, 0]

while True:
    print("\n1. Shopkeeper")
    print("2. Customer")
    print("3. Report")
    print("4. Exit")
    role = int(input("Enter your role: "))

    
    if role == 1:
        print("\n--- Shopkeeper Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Modify Item")
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter fruit name: ")
            price_val = int(input("Enter the price: "))
            qty = int(input("Enter the quantity: "))
            fruits.append(name)
            quantity.append(qty)
            price.append(price_val)
            profits.append(0)
            print(f"{name} added successfully!")

        elif choice == 2:
            name = input("Enter fruit to remove: ")
            if name in fruits:
                idx = fruits.index(name)
                fruits.pop(idx)
                quantity.pop(idx)
                price.pop(idx)
                profits.pop(idx)
                print(f"{name} removed successfully!")
            else:
                print("Item not found!")

        elif choice == 3:
            name = input("Enter fruit to modify: ")
            if name in fruits:
                idx = fruits.index(name)
                new_price = int(input("Enter new price: "))
                new_quantity = int(input("Enter new quantity: "))
                price[idx] = new_price
                quantity[idx] = new_quantity  
                print(f"{name} updated successfully!")
            else:
                print("Item not found!")

    
    elif role == 2:
        print("\n--- Customer Menu ---")
        total_bill = 0
        bought_items = []

        while True:
            print("\nAvailable Fruits:")
            for i in range(len(fruits)):
                print(f"{i+1}. {fruits[i]} - ₹{price[i]} ({quantity[i]} left)")

            choice = input("Enter fruit to buy: ")
            if choice not in fruits:
                print("Item not found!")
                continue

            idx = fruits.index(choice)
            qty = int(input("Enter quantity: "))

            if qty <= quantity[idx]:
                item_price = price[idx]
                bill = item_price * qty
                total_bill += bill
                quantity[idx] -= qty
                profits[idx] += bill
                bought_items.append((choice, item_price, qty, bill))
                print(f"Added {qty} {choice}(s) - ₹{item_price} each = ₹{bill}")
            else:
                print("Not enough stock!")

            more = input("Do you want to buy anything else? (yes/no): ")
            if more != "yes":
                break

        print("Final Bill")
        print("Item\tPrice\tQty\tSubtotal")
        for item, item_price, qty, bill in bought_items:
            print(f"{item}\t₹{item_price}\t{qty}\t₹{bill}")
        print(f"\nTotal Amount: ₹{total_bill}")
        print("*****Thank you for shopping*****")

    
    elif role == 3:
        print("--- Store Report ---")
        total_profit = 0
        for i in range(len(fruits)):
            print(f"{fruits[i]} - Sold ₹{profits[i]} | Remaining: {quantity[i]}")
            total_profit += profits[i]
        print(f" Total Profit: ₹{total_profit}")

        

    elif role == 4:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice, try again.")









