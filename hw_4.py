store_dictionary={}

while  True:
    print("1. Sell\n2. Checkout ")
    user_input=input("Make a choice: ")

    if user_input.isdigit() and int(user_input)==1:
        sold_item_name=input("Enter the sold item: ")
        sold_item_count=int(input("Enter how many sold: "))

        if sold_item_name in store_dictionary:
            store_dictionary[sold_item_name]+=sold_item_count
        else:
            store_dictionary[sold_item_name]=sold_item_count

        print(sold_item_count,sold_item_name,"sold")

        
    elif user_input.isdigit() and int(user_input)==2:
        print("End of the Day")
        print("Sold items:")

        for i,j in store_dictionary.items():
            print(j,i)

        break


    else:
        print("Wrong input")

