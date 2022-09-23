#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

one = int(input('coord x = '))
two = int(input('coord y ='))
if one>0 and two>0:
    print('1 quarter')
if one<0 and two>0:
    print('2 quarter')
if one<0 and two<0:
    print('3 quarter')
if one>0 and two<0:
    print('4 quarter')

