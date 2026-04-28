class Account:
        def __init__(self,number,balance):
            self.balance = int(balance)
            self.number = number
        def deposit(self,money):
            self.balance = self.balance + money
            return self.balance
     
        def withdraw(self,money):
             if money>self.balance:
                  print("Insufficient funds")
             else:
                  print("Success")
                  self.balance = self.balance - money
                  return self.balance
        def check_balance(self):
             print(f"Final Balance: {Account_my.balance}")

Account_my = input().split()
Account_my_name =Account_my[0]
Account_my_money =Account_my[1]

Account_my = Account(Account_my_name,Account_my_money )
test = int(input())
for i in range(test):
     data = input().split()
     name = data[0]
     money = int(data[1])
     if name == "deposit" :
          Account_my.deposit(money)
          
     if name == "withdraw":
          Account_my.withdraw(money)
Account_my.check_balance()