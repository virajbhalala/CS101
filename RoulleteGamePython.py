
import random
user=1500
bank=2000
    
def game():
    user=1500
    bank=2000
    print("your balance: " +str(user))
    print("Bank balance: " +str(bank))
    s= int(input("Please input the number between 0 and 36: "))
    if s>36:
        s= int(input("You didnt iput number greater than 36." +"\n" +"Please input the number between 0 and 36: "))
    b= int(input("input the amount that you want to bet: "))
           
    if b > user:
        b=int(input("input bet that is lower than the money that you have"))
        
    if b<user:
        user -=b
 

    else:
        r = random.randint(0,36)

        if s==r:
            
            b=b*36
            user +=b
            bank -= b
            user -= b
            bank +=b
            print("your account:"+ str( user )+ '$'+"bank account:"+ str(bank)+'$')

        else:
            print("you win/lost: "+str( user-1500))
            print("your account:"+ str( user )+ '$'+"bank account:"+ str(bank)+'$')

            

        if user !=0 & bank !=0:
            ask = input("Do you want to play it again? write 'yes' or 'no'")
            if ask =='yes':
                game()
            if ask == 'no':
                print("you win/lost: "+str( user-1500))
        
        
game()
