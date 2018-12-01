#We have 2 types of cycle in Python for and while 
#Есть 2 типа циклов в Python for (для) и while (пока)

#Let's begin with for
#Начнём с for

#s: for (new int) in (another int or range):
#s: for (новая целочисленная переменная) в (другая целочисленная переменная или длинна):

for a in range(5):
    print("Hello, I'm cycle 'for' (iteration("+ str(a) + "))")


#While 
#Syntax:
#while_condition
i = 0
while i<10:
    print (i)
    i+=2

#for_IteratorVariable_(String or list or range):
for j in 'hello world':
    if j == 'w':
        continue # Turn on next iteration
    print(j * 2, end ="")
#We can use else after for and while



