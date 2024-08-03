menu={
    "Thali" : 60,
    "Water Bottle" : 30,
    "Special" : 50,
    "Noodles" : 120,
    'Jeera rice' : 50
}
total_order=0
basket= []

print("Welcome to XYZ Restraunt")
print( 
    '''       1) Order Food
       2)View amount
       3)View Basket
       4)Exit'''
)
while True:
    choice=int(input("Enter your choice: "))
    print('-' * 50)
   
    if (choice==1):
        print('Thali : 60\nWater Bottle : 30\nSpecial : 50\nNoodles : 120\nJeera rice : 50')
        order_food= input("Enter the Name you want to order from menu: ")
       
        if order_food in menu:
            total_order += menu[order_food]
            basket.append(order_food)
            print(f'Your order {order_food} has been added')
        else:
            print(f'Your order{order_food} is currently unavailabe')
        print('-' * 50)
        
        while True:    
            another_order= input("Do you want to order anything more? (Yes/No): ")
            if another_order == 'Yes':
                items_2= input("Enter the Name you want to order: ")
                if items_2 in menu:
                    total_order += menu[items_2]
                    basket.append(items_2)
                    print(f'Tour order {items_2} has been added')
                else:
                    print(f'Your order{items_2} is currently unavailabe')
            elif another_order == 'No':
                break
                print('-' * 50)
    elif (choice==2):
        print(f'Your Total Amount: {total_order}')
    elif (choice==3):
        print(f'Your Food Basket: {", ".join(basket)}')
    elif choice==4:
        print(f'Total Payable amount: {total_order}')
        break
    
 
print('**Thank You for ordering Food Have a great Day**')    