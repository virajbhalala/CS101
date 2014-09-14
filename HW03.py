
#3.17
a, b, c = 3, 4, 5
if a<b:                     #a
    print('OK')
if c<b:
    print('OK')             #b
if (a+b)<c:
    print('OK')             #c
if (a*a+b*b)<(c*c):
    print('OK')             #d

#3.18
a, b, c = 3, 4, 5
if a<b:                     #a
    print('OK')
else:
    print('NOT OK')
if c<b:
    print('OK')             #b
else:
    print('NOT OK')
if (a+b)<c:
    print('OK')             #c
else:
    print('NOT OK')
if (a*a+b*b)<(c*c):
    print('OK')             #d
else:
    print('NOT OK')

#3
import turtle
shape= input('enter shape from one these choices: line, triangle, square')
width= int(input('enter width'))
length= int(input('enter length'))
color= input('enter color')

s = turtle.Screen()
t=turtle.Turtle()
t.pencolor(color)
t.pensize(width)

if shape=='line':
    t.forward(length)
if shape=='triangle':
    for i in range(3):
        t.forward(length)
        t.right(120)
if shape=='square':
    for i in range(4):
        t.forward(length)
        t.right(90)
