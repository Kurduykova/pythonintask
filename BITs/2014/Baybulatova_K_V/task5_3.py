#Задача 4. Вариант 3.
#Программа, которая при запуске случайным образом отображала  название одного из цветов радуги

#Байбулатова К.В.
#14.03.2016

import random
Один="Красный"
Два="Оранжевый"
Три="Желтый"
Четыре="Зеленый"
Пять="Голубой"
Шесть="Cиний"
Семь="Фиолетовый"
print("Программа случайным образом отображает  название одного из цветов радуги")
a=random.randint(1,7)
if(a==1):
	print(Один)
elif(a==2):	
	print(Два)
elif(a==3):
	print(Три)
elif(a==4):
	print(Четыре)
elif(a==5):
	print(Пять)
elif(a==6):
	print(Шесть)
elif(a==7):
	print(Семь)
input('Нажмите Enter для выхода')	