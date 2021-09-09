class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is :-")
        print("Withdraw1 = 100")
        print("Withdraw2 = 500")
        print("Withdraw3 = 2000")

    def withdrawl1(self,Withdraw1):
        new_amount = 100 - Withdraw1
        print("You have withdrawn amount :- "+str(Withdraw1) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl2(self,Withdraw2):
        new_amount = 500 - Withdraw2
        print("You have withdrawn amount :- "+str(Withdraw2) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl3(self,Withdraw3):
        new_amount = 2000 - Withdraw3
        print("You have withdrawn amount :- "+str(Withdraw3) + ". Your remaining balance is "+ str(new_amount))        


def main():
    print("Welcome to the Bank!")
    Card_number = input("Insert your Card number:- ")
    Pin_number  = input("Enter your pin number:- ")

    new_user =  Atm(Card_number,Pin_number)

    print("Choose")
    print("1.Balance Enquriy    2.Withdrawl")
    activity = int(input("Enter the number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. Add Withdraw1")
        print("2. Add Withdraw2")
        print("3. Add Withdraw3")
        choose = int(input("1. Add Withdraw1  2. Add Withdraw2 3. Add Withdraw3: "))
        if (choose == 1):
           Withdraw1 = int(input("Enter the amount:- "))
           new_user.withdrawl1(Withdraw1)
        if (choose == 2):
           Withdraw2 = int(input("Enter the amount:- "))
           new_user.withdrawl2(Withdraw2)    
        if (choose == 3):
           Withdraw3 = int(input("Enter the amount:- "))
           new_user.withdrawl3(Withdraw3)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()