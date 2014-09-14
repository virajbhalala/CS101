
def stats(file):
    f=open(file)
    words= len(str.split(f.read()))
    
    count=0
    countChar=0
    #dont know why this for loop is not executing
    for lines in f.read():
        count =count+1       
        countChar=countChar+len(line)
        
    print("lines count " + str(count))
    print("words count " + str(words))
    print("characters count "+ str(countChar))
    
stats('example.txt')
