import time
space = " "
p=space*8
ingredient_list=["chocolate", "milk", "flour", "sugar" ]
response_sheet=[ ]
score = 0
s = "Welcome To Ingredients World"
for i in range(2):
    i= 72 + 16
    print("*" * i)
l=72 + 10
y=space*l
z=space*27
print("***" + y + "***")
print("***" + z + s + z + "***")
print("***" + y + "***")
q=space*31
print("*" * i)
text_to_print="what is your name ? "
tag=(88-len(text_to_print)) / 2 
tag_1=space * int(tag)             
print("***"+q+ text_to_print+q+"***")

username=input("                             response: ")
print(p+"Hello " + username + " ! you have to guess 3 ingredients from the cookies recipe")

continue_the_game = "yes" 
time.sleep(2)
while continue_the_game == "yes":
    for i in range(3):
        i+=1
        text_to_print="guess ingredient " +  str(i) + space
        tag=(88-len(text_to_print)) / 2 
        tag_1=space * int(tag)             
        print(str(tag_1) + text_to_print)
        
        ingredient= input("                             response: ")
        if ingredient in ingredient_list:
            if ingredient not in  response_sheet :
                text_to_print="wow, congratulations"
                tag=(88-len(text_to_print)) / 2 
                tag_1=space * int(tag)             
                print(str(tag_1) + text_to_print)
                score = score + 1
                response_sheet.append(ingredient)
            else:
                text_to_print="repeated answer!!!"
                tag=(88-len(text_to_print)) / 2 
                tag_1=space * int(tag)             
                print(str(tag_1) + text_to_print)
                
        else:
            text_to_print="oups, error!"
            tag=(88-len(text_to_print)) / 2 
            tag_1=space * int(tag)             
            print(str(tag_1) + text_to_print)
            
    text_to_print="Game over! congratulations " + username + " you have " + str(score) + " points"
    tag=(88-len(text_to_print)) / 2 
    tag_1=space * int(tag)  
    
    text_to_print_1="Game over! congratulations " + username + " you have " + str(score) + " point"
    tag=(88-len(text_to_print_1)) / 2 
    tag_1=space * int(tag)            
    
    print(str(tag_1) + text_to_print) if score > 1 else print(tag_1+text_to_print_1)
    
    text_to_print=username + " do you want to continue? "
    tag=(88-len(text_to_print)) / 2 
    tag_1=space * int(tag)             
    print(str(tag_1) + text_to_print)
    continue_the_game= input("                             response: ")
    
text_to_print="The ingredient_list was:"
tag=(88-len(text_to_print)) / 2 
tag_1=space * int(tag)             
print(str(tag_1) + text_to_print)

time.sleep(2)

text_to_print=str(ingredient_list)
tag=(88-len(text_to_print)) / 2 
tag_1=space * int(tag)  
           
print(str(tag_1) + text_to_print)

i= 72 + 16
print("*" * i)
text_to_print="see you next time"
tag=(88-len(text_to_print)) / 2 
tag_1=space * int(tag)            
 
print(str(tag_1) + text_to_print)

for i in range(2):
        i= 72 + 16
        print("*" * i)


    