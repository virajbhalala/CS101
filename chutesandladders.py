import random
ladders={1:38,4:12, 9:31, 21:42, 28:84, 36:44, 51:67,71:90, 80:100}
chutes ={16:6, 48:20, 49:11, 56:53, 62:10, 64:60, 87:24, 93:73, 95:75, 98:78}
pos=0
def rollDie():
    return random.rantint(1,12)
def checkCL(p):
    if p in ladders:
        return ladders[p]
    elif p in chutes:
        return chutes[p]
    else:
        return p
def move(roll):
    global pos
    pos +=roll
    pos = checkCL(pos)
    
    
def main():
    while pos<100:
        move(rollDie())
    
