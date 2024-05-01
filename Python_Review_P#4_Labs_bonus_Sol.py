while True:
    try:
        username = input("Please enter your name: ")
        age = int(input("Please enter your age: "))

        if age > 0 and age <= 6:
            print("Kid")
        elif age < 0:
            print("Wrong age value, you can not enter value 0 or less.")

        elif age > 6:
            total_cost = 0.00

            itemsLen = int(input("Please enter the number of items you want to buy: "))
            for i in range(itemsLen):
                item_name = input("Item name: ")
                item_price = float(input("Item price: "))
                item_quantity = int(input("Item quantity: "))

                total_cost += item_price * item_quantity
                print("the item total cost is",item_price * item_quantity)

            print("the total cost of your purchases is", total_cost)
            if total_cost > 20:
                total_cost = total_cost * 1.2
                print("Since you are a special customer we will give 20% discount!!", total_cost)
            
            print("thank you for your purchase <3")
        break

    except ValueError:
        print("Invalid input! Please enter a valid value.")
        repeat = input("Do you want to repeat the process? (yes/no): ")
        if repeat.lower() != 'yes' and repeat.lower() != 'y':
            break