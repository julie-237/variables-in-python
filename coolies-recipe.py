import time
ingredient_list=["chocolate", "milk", "flour", "sugar" ]
response_sheet=[ ]
score = 0
print("**********************************")
print("**                              **")
print("** Welcome To Ingredients World **")
print("**                              **")
print("**********************************")
username=input("what is your name?")
print("Hello " + username + " ! you have to guess 3 ingredients from the cookies recipe")

continue_the_game = "yes" 
time.sleep(2)
while continue_the_game == "yes":
    for i in range(3):
        i+=1
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
    print("Game over! congratulations " + username + " you have " + str(score) + " points") if score > 1 else print("Game over! congratulations " + username + " you have " + str(score) + "point")
    print("The ingredient_list was:")
    time.sleep(2)
    print(ingredient_list)
    continue_the_game= input(username + " do you want to continue? ")
print("ok, see you next time")


    