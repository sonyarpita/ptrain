from random import randint
class BankAccount:
    '''userName=""
    aadharNumber=0
    accountNumber=0
    initialBalance=0
    '''
    def __init__(self):
        self.username=input("Enter Username ")
        self.aadharNumber=int(input("Enter aadhar number "))
        self.accountNumber=randint(0,999999999999)
        self.initialBalance=float(input("Enter initial deposit amount "))
    
    def UserInfo(self):
        print("Username= ",self.username)
        print("aadharNumber= ",self.aadharNumber)
        print("A/C Number= ",self.accountNumber)
        print("Current Balance= ",self.initialBalance)
    
    def Withdraw(self,amount):
        self.initialBalance=self.initialBalance-amount
        return self.initialBalance
    
    def Deposit(self,amount):
        self.initialBalance=self.initialBalance-amount
        return self.initialBalance

    #def ChangeDetails(self):
    #    self.
    
#    def MiniStatement(self):

    
    #def MiniStatement():
#        return self.initialBalance

'''user1=BankAccount()
print("-----------user details:-----------")
user1.UserInfo()
'''

while True:

    user_input=int(input("Enter type of service required - \n 1. Enter 1 to create new account \n 2. Enter 2 for User Info \n 3. Enter 3 to Withdraw \n 4. Enter 4 to Deposit \n 5. Enter 0 to exit \n"))
    
    try:
        if user_input==1:
            user1=BankAccount()
            print("-----------user details:-----------")
            user1.UserInfo()
    

        elif user_input==2:
            print("-----------user details:-----------")
            user1.UserInfo()

        elif user_input==3:
            amount_to_withdraw=float(input("Enter amount to withdraw: "))
            print("Balance available after a withdrawal = ",user1.Withdraw(amount_to_withdraw))

        elif user_input==4:
            amount_to_deposit=float(input("Enter amount to deposit: "))
            print("Balance after depositing= ",user1.Deposit(amount_to_deposit))
            print("Final Balance = ",user1.initialBalance)
    
        elif user_input==0:
            exit()
    
    except UserNotFound:
        print("User Not Found, please create account")
