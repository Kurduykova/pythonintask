﻿#Задача 5. Вариант 6.
#Напишите программу, которая бы при запуске случайным образом отображала название одного из двух спутников Марса.

#Данилов Д.А.
#21.05.2016
import random
first="Фобос"
second="Дэймос"

print("Программа случайным образом отображала название одного из двух спутников Марса")
a=random.randint(1,2)
if(a==1):
	print(first)
elif (a==2):
	print(second)

input("\n\n\nНажмите Enter для завершения")
