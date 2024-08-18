#name = input("what's your name? ")
#print("hello " + name)
#user_age = int(input("how old are you?"))
#future_user_age = user_age +  10
#print("In 10 years you will be " + str(future_user_age))

import time
name = input("what's your name?")
print("hello " + name)
time.sleep(2)
goods_sold = int(input("howmany goods have you sold today?"))
print ("you have sold " + str(goods_sold) + " goods today")
time.sleep(2)
goods_leftover = int(input("how many goods are left?"))
print ("so you have " + str(goods_leftover) + " goods left")
time.sleep(2)
total_goods = goods_sold + goods_leftover
print ("so you initially had " + str(total_goods) + " goods")