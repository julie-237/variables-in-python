import time
ingredient_list=["chocolate", "milk", "flour", "sugar" ]
score = 0
print("Hello! you have to guess 3 ingredients from the cookies recipe")
time.sleep(3)
ingredient_1= input("guess ingredient 1 ")
if ingredient_1 in ingredient_list:
    print("wow, congratulations")
    score += 1
else:
    print("oups, error!")
time.sleep(2)

ingredient_2= input("guess ingredient 2 ")
if ingredient_2 in ingredient_list:
    print("wow, congratulations")
    score = score + 1
else:
    print("oups, error!")
time.sleep(2)
    
ingredient_3= input("guess ingredient 3 ")
if ingredient_3 in ingredient_list:
    print("wow, congratulations")
    score = score + 1
else:
    print("oups, error!")
    
time.sleep(2)
print("Game over! you have " + str(score) + "points")
print("The ingredient_list was:")
time.sleep(2)
print(ingredient_list)
    