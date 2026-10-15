Inventory = { "Rice": 50, "Oil": 30, "Sugar": 20, "Tea": 15}

while True:
    print("1. Sell product")
    print("2. Add new product")
    print("3. Show inventory")
    print("4. Low inventory")
    print("5. Exit")

    choice = int(input("Your choice: "))


    if choice == 1 :
        name = input("Product name: ")
        count = int(input("Quantity: "))

        if count <= 0 :
            print("Quantity must be greater than zero!")

        elif name in Inventory:
            if Inventory[name] >= count:
                Inventory[name] -= count
                print("Sale successful")
            else:
                print("Not enough inventory")

        else:
            print("Product not found")


    elif choice == 2 :
        name = input("Product name: ")
        count = int(input("Quantity: "))

        if not name: 
            print("Product name is cannot be empty.")

        elif count <= 0 :
            print("Quantity must be greater than zero.")

        elif name is Inventory :
            Inventory[name] += count
            print("Pruduct quantity updated.")

        else: 
            Inventory[name] = count
            print("product added.")


    elif choice == 3 :
        for name in Inventory:
            print(name,Inventory[name])


    elif choice == 4 :
        for name in Inventory:
            if Inventory[name] < 10:
                print("Warning!!!")
                print(name,Inventory[name])


    elif choice == 5 :
        print("Goodbye")
        break

    
    else :
        print("Wrong choice")