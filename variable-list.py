grocery_list = ["milk", "sugar", "chocolate", "honey"]
fruit_list = ["banana", "apple", "orange","mango"]
temperature_list = [20.4, -12.8 ]

client_order = input("which fruit do you want ?")
if client_order not in fruit_list:
    print("we don't have " + client_order)
    exit()
    
    print("ok")

"""if client_order in fruit_list:
    print("you can get it")
else:
    print("we don't have " + client_order)"""

print(grocery_list)
#print(len(grocery_list))
#print(temperature_list)

grocery_list[3] = "beer"
#print(grocery_list[4])
print(grocery_list)
grocery_list.append("butter")
print(grocery_list)

if "milk" in grocery_list:
    print("ok")

