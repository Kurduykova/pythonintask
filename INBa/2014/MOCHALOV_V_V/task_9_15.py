﻿# -*- coding: UTF-8 -*-
# Задача 9. Вариант 15.
# 
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.
# Mochalov V. V.
# 14.05.2016

import random
WORDS=("питон","анаграмма","простая","сложная","ответ","подстаканник","абсолютный","честность",
       "авторитетный","мнение", "поступить","академия", "оранжевый","апельсин", "громкий","аплодисменты",
       "цирк","арена", "приятный","аромат", "атака", "благоприятный","атмосфера", "старинный","балкон",
       "бархатный","скатерть", "играть","баскетбол", "безвкусный","конфета", "беречь","имущество", "беседовать",
       "профессия", "размешиват","бетон", "разглядывать", "бинокль", "благородный", "поступок", "прочитать","брошюра")
word=random.choice(WORDS)
print("В загаданном слове ",len(word) ," букв.")
q=0
k=0
while k<5:
 b=input("Назовите букву: ")
 for i in word:
     if i==b:
         q=1
 if q==1:
     print("Да")
     q=0
 else:    
     print("Нет")
 k=k+1
b=input("Отгадывайте слово: ")
if b==word:
    print("Вы угадали.")
else:
    print("Вы не угадали.")
input("Для выхода нажмите Enter.")
