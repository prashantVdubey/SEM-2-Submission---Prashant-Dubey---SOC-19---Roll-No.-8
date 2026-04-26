class BankAccount :    
    def _init_(self,acc,balance):
            self.acc = acc
            self.balance = balance
            
    def deposit(self):
            amt = float (input("Enter the amount you want to deposit: "))
            self.balance = self.balance + amt
            print (f"The {self.acc} account  has a total balance of amount {self.balance}")
            
    def withdraw(self):
            amt = float (input("Enter the amount you want to withdraw: "))
            if amt<=self.balance :
                    self.balance= self.balance-amt
                    print (f"Amount {amt} is withdrawn from account : {self.acc}")
            else: 
                    print("Insufficient balance ")
                    
    def check_balance (self):
            print (" Balance : " , self.balance )
            
acc= input("Enter your account number :  " ) 
balance = float (input ("Enter initial balance: "))
obj = BankAccount(acc,balance)

while True :
        print ("\n1 : deposit")
        print ("2 : withdrawn " )
        print ("3 : check_balance  " )
        print ("4 : Exit " )
        
        operation = input (" Enter the number for the valid operation :")

        if operation == "1":
                obj.deposit()
        elif operation == "2":
                obj.withdraw()
        elif operation == "3":
                obj.check_balance()
        else :
                break
