import time
ingredient_list=["chocolate", "milk", "flour", "sugar" ]
response_sheet=[ ]
score = 0
print("Hello! you have to guess 3 ingredients from the cookies recipe")
time.sleep(3)

for i in range(3):
    i +=1
    ingredient= input("guess ingredient  " + str(i))
    if ingredient in ingredient_list:
        if ingredient not in  response_sheet :
            print("wow, congratulations")
            score = score + 1
            response_sheet.append(ingredient)
        else:
            print("repeated answer!!!")
    else:
         print("oups, error!")
        
    
time.sleep(2)
print("Game over! you have " + str(score) + " points") if score > 1 else print("Game over! you have " + str(score) + "point")

print("The ingredient_list was:")
time.sleep(2)
print(ingredient_list)
    