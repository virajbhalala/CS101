def commonCharacter(text1,text2):
    s=''
    for i in text1:
        for j in text2:
            if i == j:
                if(i not in s):
                    s +=i
                
    return s
seussLine = 'The cat in the hat came back.'
searchLetters = 'ac'
print(commonCharacter(seussLine, searchLetters))
