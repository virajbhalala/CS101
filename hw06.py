
#4.27
def fcopy(firstFile,secondFile):
    file1 = open(firstFile, 'r')
    file2=open(secondFile, 'w')#assuming we are erasing the content of the file and writing in it.
    file2.write(file1.read())
    file2=open(secondFile)
    return file2.read()
    file1.close()
    file2.close()
    
print(fcopy('example.txt','output.txt'))
    
#4.29

def stats(file):
    f=open(file)
    words= len(str.split(f.read()))
    
    count=0
    countChar=0
    #dont know why this for loop is not executing :(
    for lines in f.read():
        count =count+1       
        countChar=countChar+len(lines)
        
    print("lines count: " + str(count))
    print("words count: " + str(words))
    print("characters count: "+ str(countChar))
    
stats('example.txt')

#3
import string
def repeatWords(firstFile,secondFile):
    file1 = open(firstFile, 'r')
    file2=open(secondFile, 'w+')
    
    for line in file1:
        #lower case line
        line.lower()
        #removes punctuation
        for c in string.punctuation:
            line.replace(c,'')
        words = line.split()
        
        temp=''
        for word in words:
            num =words.count(word)
            if num>1:
                #find if word is repeated.if not then write it
                if temp.find(word)==-1:
                    file2.write(word+ " ")
                    temp=temp+word
        #next line  
        file2.write("\n")
    file2=open(secondFile)
    return file2.read()
    file1.close()
    file2.close()

print(repeatWords('example.txt','new.txt'))
            
    
    
