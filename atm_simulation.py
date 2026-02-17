balance=1000
pin = 890
locked = False

def user():
    global locked
    
    if locked:
        print('Account is Locked !')
        return False   # <-- STOP execution immediately

    attempt = 0
    
    while attempt < 3:
        pin_num = int(input("enter 3 digit pin: "))
        
        if pin_num != pin:
            print("wrong pin try again!!")
            attempt += 1
        else:
            print("login successful")
            return True

    locked = True
    print("wrong pin attempt try again tomorrow or contact nearest branch")
    return False


def menu():
    if user():
        while True:
            print("Enter 1: withdraw")
            print("Enter 2: check balance")
            print("Enter 3: deposit")
            print("Enter 4: exit")
            
            query=int(input("enter any of the about number: "))
            if query==1:
                withdraw()
            elif query==2:
                print("current balance :",balance)
            elif query==3:
                deposit()
            elif query==4:
                print("Thnaks for using Aaj Nagad Kal Udhaar Bank !")
                break


def withdraw():
    global balance
    withdrawal=int(input("enter amout to withdraw: "))
    if withdrawal>balance:
        print("sorry ! your account balance is less than the amount you entered")
    else:
        balance-=withdrawal
        print("withdrawal successful !! \n current balance : ",balance)
def deposit():
    global balance
    depo=int(input("enter amount to deposit:"))
    if depo>2000:
        print("amount limit exceeded !! ")
    else:
        balance+=depo
        print("total balance now : ",balance)



menu()

        


        
        
        
        
        
