def getName():
    try:
        name_input = str(input("Please enter your name: \n>> "))
        if not name_input.isalpha():
            raise ValueError
    except ValueError:
            print("really what is your name?")
            return getName()
    return name_input

def getAge():
    try:
        age_input = int(input("Please enter your age: \n>> "))
    except ValueError:
            print("really how old are you?")
            return getAge()
    return age_input

def getNum():
    try:
        num_input = int(input("how many items you want to buy? \n>> "))
    except ValueError:
            print("man, really how many?")
            return getNum()
    return num_input

def get_valid_item_info(prompt, input_type):
    try:
        user_input = input(prompt)
        item = input_type(user_input)
        if input_type == str and not str(item).isalpha():
            raise ValueError
    except ValueError:
        print("You Serious?")
        return get_valid_item_info(prompt, input_type)
    return item
     
while(True):
    name = getName()
    age = getAge()
        
    if 0 < age < 6:
        print("Kid! get out")
        break
    elif age < 0:
        print("Wrong age value, you can not enter value 0 or less.")
    else:
        total_cost = 0
        n_of_items = getNum()

        names_of_items = []
        price_of_items = []
        quantity_of_items = []
        for i in range(n_of_items):
            
            item_name = get_valid_item_info("Item Name?\n>> ", str)
            item_price = get_valid_item_info("Item Price?\n>> ", float)
            item_quantity = get_valid_item_info("Quantity?\n>> ", int)
    

            names_of_items.append(item_name)
            price_of_items.append(item_price)
            quantity_of_items.append(item_quantity)

            item_cost = item_price * item_quantity
            total_cost += item_cost
            print(f'item cost: {item_cost}\ntotal cost: {total_cost}')

        # out of scope (for fun)
        cart = {names_of_items[i]: [price_of_items[i], quantity_of_items[i]] for i in range(len(names_of_items))}
        if total_cost > 200:
            total_cost - (total_cost * 0.2)
        
        # out of scope (for fun) 2
        print("Your receipt:")
        print("Item | Price | Quantity | Cost: ")
        print(cart)
        for k,v in cart.items():
            print(f"{k} | {v[0]} | {v[1]} | {v[0] * v[1]}")
        print(f'''----------------
   Total: {total_cost}''')

        repetetion = input("Would you like to repeat the experience? (type yes to repeat) \n>>").istitle
        if repetetion != "Yes":
             break
        
            

            


            
