
#11
import turtle
def fatline(t,segments,increment):
    fat=increment
    s=turtle.Screen()
    for i in range(5):
        fat +=increment
        t.pensize(fat)
        t.forward(50)
tur=turtle.Turtle()
fatline(tur,10,10)
#part B
def getNumber():
    number= input('enter number')
    return number

print(int(getNumber())+int(getNumber()))

#12
def countLetters(text,collection):
    ctr=0
    for i in text:
        for j in collection:
            if i == j:
                ctr +=1
    return ctr
seussLine = 'The cat in the hat came back.'
searchLetters = 'ac'
print(countLetters(seussLine, searchLetters))
#13
#I am assuming it method returns largest number
def getNumer(lower,upper):
    num=int(input('Please give number between '+ lower +' and ' +upper))
    return num
#partB
a=getNumber(1,100)
b=getNumber(1,100)
print(a+b)
