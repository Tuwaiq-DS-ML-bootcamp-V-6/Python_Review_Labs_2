


user_here=True
while user_here:
    try:
        name=input("please Enter you name = ")
        age=int(input("please Enter your age = "))
    except:
        print("please Re-Enter your age correctly: ")
        age = int(input())
    
    if 0<age<=6:
        print("Kid") 
    elif 0>=age:
        print("Wrong age value, you can not enter value 0 or less.")
    else :
        user_still_here=True
        total_cost=0
        while (user_still_here):
            try:
                
                item_name=input("Please enter the name of item : ")
                item_price=float(input("please enter item price : "))
                item_quantity=int(input("please enter items quantity : "))
            

                item_total_cost=item_price*item_quantity
                total_cost+=item_total_cost
                print('item total cost= ',item_total_cost, '\ntotal cost ', total_cost )
                if total_cost>=200:
                    total_cost-= total_cost*0.2
                    print("the total cost after discound is = ", total_cost)
                print("do you want to continue shopping? y/n")
                answer = input()
                if answer == 'y':
                    user_still_here=True
                else :
                    user_still_here=False
            except:
            
                item_price=float(input("please Re-enter item price correctlly : "))
                item_quantity=int(input("please Re-enter items quantity correctlly : "))


                item_total_cost=item_price*item_quantity
                total_cost+=item_total_cost
                print('item total cost= ',item_total_cost, '\ntotal cost ', total_cost )
                if total_cost>200:
                    total_cost-= total_cost*0.2
                print("do you want to continue shopping? y/n")
                answer = input()
                if answer == 'y':
                    user_still_here=True
                else :
                    user_still_here=False
        print("Thanks for shopping from us.. have a good day! ")
