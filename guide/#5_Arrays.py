#!Arrays (lists) in Python
#!Массивы (листы) в Python

a = [5,3,9,17,21] #Объявляем массив || Create a list (array)


#This is list
#Это лист
print( a[2], "Second index from 0, it's 9" ) #First index of list - 0
print( a[3], "Третий индекс от 0, это 17" ) #Первый индекс листа - 0

#If u want to print 5, from our massive, u have to input 0
#Если ты хочешь вывести 5 из нашего массива, тебе нужно ввести 0
print( a[0] ) #5
print( a[1] ) #3
print( a[2] ) #9
print( a[3] ) #17
print( a[4] ) #21

#If you want to print 9 and upper:
#Если ты хочешь вывести 9 и выше:
print(a[2:])

#You can change every value:
#Вы можете изменять каждое значение:
a [2] = 15
print(a[2])


#If you wanna print 3 - 21:
#Если вы хотите вывести с 3 по 21:
print(a[1:4])

input("Nevermind, press Enter to quit")