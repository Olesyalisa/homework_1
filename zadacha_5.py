#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

# по теореме Пифагора (((x-x2)**2)+(y-y2)**2)2)
from math import sqrt

xA = float(input('one_point A: '))
yA = float(input('two_point A: '))

xB = float(input('one_point B: '))
yB = float(input('two_point B: '))

interval = float(sqrt((xA-xB)**2+(yA-yB)**2))
print(round(interval,2))
