



def binarySearch (x,lst):
    newlst=lst
    for i in range(len(lst)//2):
        middle= newlst[len(newlst)//2]
        if x==middle:
            return 'true'
        elif x<middle:
            newlst= newlst[:len(newlst)//2]
        else:
            newlst=newlst[len(newlst)//2:len(newlst)]
            
print(binarySearch (9,[1,3,4,6,7,8,9]))
        
        
        
    
