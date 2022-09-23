#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('enter digit: '))
print(quarter>1 or quarter<4)
if quarter == 1:
    print('x>0 and y>0')
if quarter == 2:
    print('x<0 and y>0')
if quarter == 3:
    print('x<0 and y<0')
if quarter == 4:
    print('x>0 and y<0')