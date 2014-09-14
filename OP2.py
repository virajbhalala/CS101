

#13

def droplets(t,size,seperations):
    pos=0
    for i in range(len(seperations)+1):
        t.circle(size)
        t.penup()
        pos=pos+seperations[i]
        t.goto(pos,0)
        t.pendown()
import turtle
turt = turtle.Turtle()
droplets(turt, 5, [20, 25, 30])

#14
def mostlyVowels(s):
    ary=s.lower().split()
    newAry=[]
    vowels= ['a','e','i','o','u']
    for word in ary:
        ctr=0
        for v in vowels:
            ctr=ctr+word.count(v)
            if (ctr>len(word)/2):
                newAry.append(word)
    return newAry
mlk = 'Our lives begin to end the day we become silent about things that matter'
print(mostlyVowels(mlk))

#15
def duplicateWords(inFile,outFile):
    f=open(inFile)
    read=f.read()
    ary=read.split()
    write=open(outFile, 'w+')
    for i in ary:
        if ary.count(i)>1:
            write.write(i+ " " + str(ary.count(i)) + "\n")
            ary.remove(i)
    write=open(outFile)
    print(write.read())
inF = 'hatCat.txt'
outF = 'hatCatDuplicateWords.txt'
duplicateWords(inF, outF)
            
        
        
    
    
    
