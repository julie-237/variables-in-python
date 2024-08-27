width = 100
design_1 = "*"
design_2 = "***"
text_to_print = ("")
space = " "
spacing = space * int(((width - len(text_to_print))/2) - (len(design_2)*2))
design_1_spacing = space*(width - (len(design_2))*2)
line_1 = design_1 * width
line_2 = design_2 + design_1_spacing + design_2
line_3 = design_2 + spacing + text_to_print + spacing + design_2










score = 0
Ingredient_list = ["milk", "sugar", "flour", "eggs", "butter", "chocolate"]
Answer_sheet = []
print("\n")
for i in range(2):
    print(line_1)
print(line_2)
text_to_print = "welcome To Ingredients World"
spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
print(line_2)
print(line_1)

text_to_print = "what is your name ? "
spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
#if len(text_to_print)%2 != 0:
print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
username = input(design_2 + spacing + "response: ")

text_to_print = "Hello " + username + " ! You have to guess 3 ingredients from the cookies recipe"
spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)

text_to_print = "Are you ready ? "
spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
response = input(design_2 + spacing + "response: ")

while response == "yes":
    for i in range(3):
        i+=1
        text_to_print = "Guess ingredient " + str(i)
        spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
        print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
        Answer = input(design_2 + spacing + "response: ")
        if Answer in Ingredient_list:
            if Answer not in Answer_sheet:
                text_to_print = "Wow, Congratulations!!!"
                spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
                print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
                score = score + 1
                Answer_sheet.append(Answer)
            else:
                text_to_print = "Repeated answer!!"
                spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
                print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
        else:
            text_to_print = "Oups, Failed!"
            spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
            print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
            
    text_to_print = "Game over! " + ("Congratulations " if score != 0 else "Sorry " ) + username + " you have " + str(score) + " point" + ("s" if score>1 else "")
    spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
    print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
    
    text_to_print = username + " do you wish to continue ? "
    spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
    print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
    response = input(design_2 + spacing + "response: ")
    
text_to_print = "The ingredient_list was :" + str(Ingredient_list)
spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)

text_to_print = "see you next time"
spacing = space * int(((width - len(text_to_print))/2) - len(design_2))
print(line_1)
print(design_2 + spacing + text_to_print + (" " if len(text_to_print)%2 != 0 else "") + spacing + design_2)
for i in range(2):
    print(line_1)
print("\n")
            
