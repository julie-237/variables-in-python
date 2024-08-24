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
print("*" * i)
text_to_print="what is your name ? "
tag=(88-len(text_to_print)) / 2 
tag_1=space * int(tag) 
q=space*int((88-len(text_to_print)-6) / 2 ) 
q1=space*int(tag/5)        
print("***"+q+ text_to_print+q+"***")

username=input("***"+q+"response: "+q+"***")
print("***"+q1+"Hello " + username + " ! you have to guess 3 ingredients from the cookies recipe"+q1+"***")

continue_the_game = "yes" 
time.sleep(2)
while continue_the_game == "yes":
    for i in range(3):
        i+=1
        text_to_print="guess ingredient " +  str(i) + space             
        print("***"+q + text_to_print+q+" ***")
        
        ingredient= input("                             response: ")
        if ingredient in ingredient_list:
            if ingredient not in  response_sheet :
                text_to_print="wow, congratulations"            
                print("***"+q+ text_to_print+q+"***")
                score = score + 1
                response_sheet.append(ingredient)
            else:
                text_to_print="repeated answer!!!" 
                tag=(88-len(text_to_print)) / 2 
                tag_1=space * int(tag) 
                q=space*int((88-len(text_to_print)-6) / 2 )          
                print("***"+q+ text_to_print+q+"***")
                
        else:
            text_to_print="oups, error!"  
            tag=(88-len(text_to_print)) / 2 
            tag_1=space * int(tag) 
            q=space*int((88-len(text_to_print)-6) / 2 )           
            print("***"+q+ text_to_print+q+"***")
            
    text_to_print="Game over! congratulations " + username + " you have " + str(score) + " points" 
    tag=(88-len(text_to_print)) / 2 
    tag_1=space * int(tag) 
    q=space*int((88-len(text_to_print)-6) / 2 ) 
    
    text_to_print_1="Game over! congratulations " + username + " you have " + str(score) + " point"
    tag=(88-len(text_to_print_1)) / 2 
    tag_1=space * int(tag) 
    q=space*int((88-len(text_to_print_1)-6) / 2 )           
    
    print("***"+q+ text_to_print+q+"***") if score > 1 else print("***"+q+ text_to_print_1+q+"***")
    
    text_to_print=username + " do you want to continue? " 
    tag=(88-len(text_to_print)) / 2 
    tag_1=space * int(tag) 
    q=space*int((88-len(text_to_print)-6) / 2 )            
    print("***"+q+ text_to_print+q+"***")
    continue_the_game= input("                             response: ")
    
text_to_print="The ingredient_list was:"
tag=(88-len(text_to_print)) / 2 
tag_1=space * int(tag) 
q=space*int((88-len(text_to_print)-6) / 2 ) 
print("***"+q+ text_to_print+q+"***")

time.sleep(2)

text_to_print=str(ingredient_list)
tag=(88-len(text_to_print)) / 2 
tag_1=space * int(tag) 
q=space*int((88-len(text_to_print)-6) / 2 )             
print("***"+q+ text_to_print+q+"***")

i= 72 + 16
print("*" * i)

text_to_print="see you next time" 
tag=(88-len(text_to_print)) / 2 
tag_1=space * int(tag) 
q=space*int((88-len(text_to_print)-6) / 2 )         
print("***"+q+ text_to_print+q+"***")

for i in range(2):
        i= 72 + 16
        print("*" * i)


    