#28/10/2021
#pavithra
#create a shopping cart




    
#def Admin():
        
def selection():
    while True:
            
                print("\n 1.Add\n 2.Delete\n 3.Exit")
                select1=input("Enter your choice:")
                if select1 == '1':
                    add_item()
                elif select1 == '2':
                    delitem()
                elif select1 == '3':
                    main()



def cus():
       print("      ----------------Welcome to Online Purchese----------------------")
       print("\n 3.Purchese\n 4.userdelitem\n 5.Exit\n ")
       
       select=input("Enter your choice : ")
       #print(Item)


       if select=='3':
          user_login()
            
       if select=='4':
          userdelitem()

       if select=='5':
          main()   


       for x in Item:
            print(x)
def add_item():
    while True:
        additem=input("Enter the add item : ")
        if additem not in Item or additem in Item:
           Item.append(additem)
           print(Item)

           addquantity=input("Enter the add quantity of item : ")
        if addquantity not in Quantity or addquqantity in Quantity:
           Quantity.append(addquantity)
           print(Quantity)

           addprice=input("Enter the add price of item : ")
        if addprice not in Prices or addprice in Prices:
           Prices.append(addprice)
           print(Prices)

           #main()


           next=input("Let's go to Add? (y\/n):")
           if next=='y':
               add_item() 

            
           if next=='n':
               main()

           #useritem()


def delitem():
    shop=input("delete item :")
    a=Item.index(shop)
    del Item[a]
    print(Item)

 

def userdelitem():
    while True:
        print(Item)
        tool=input("User delete item : ")
        a1=Item.index(tool)
        del Item[a1]
        print(Item)
        print("Your Order Deleted Successfully")

        main()

        #next=input("Let's go to purchase? (y\/n):")
        #if next=='n':
         #   break
        #purchaseitem()

def user_login():
    
    cart1=input("Enter your EmailId: ")
    cart2=input("Enter your Password: ")
    cart2=input("Enter your Pin: ")

    purchase_item()
    
    print(Item)
    
def purchase_item():
    shop=[]
    print(Item)
    section=input("Enter the item : ")            

    if section in Item:
        user=int(Item.index(section))
        shop.append(user)
        print("Your shopping list : ",shop)
        qty=int(input("Enter the quantity : "))
        text=Quantity[user]
        Total_qty=int(text)-int(qty)
        price=int(qty)*int(Prices[user])
        print("Remaing the qty : " ,str(Total_qty))
        print("Pay the price: " ,str(price))
        print("Your Order is Successfully\n")
        print("   ----------------------------  Thank You To Purchase..... -------------------\n")

    next=input("Let's go to Purchase? (y\/n):")
    if next=='y':
        purchase_item()
    if next=='n':
        main()
          


        #cus()
                    
Item=['saree','chain','ring','chudi','long dress']
Quantity=[100,600,250,180,550]
Prices=[50,10,60,45,30]



def main():
    print("        ---------------Welcome Our Onine Shopping----------------")
    while True:
        print("\n 1.Admin\n 2.User\n 3.Exit ")
        
        select=input("Select your option: ")
        if select == '1':
            selection()
        elif select == '2':
            cus()
        elif select == '3':
            break


admin_name=['karthik','dharani','preveenkumar']
admin_password=['123','456','789']




main()
    
