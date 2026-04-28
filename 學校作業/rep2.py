class Account:
  def __init__(self,number,balance):
    self.number = number
    self.balance = int(balance)
  def deposit(self,money):
    self.balance += money
  def withdraw(self,money):
    if money>self.balance:
      print("Insufficient funds")
    else:
      print("Success")
      self.balance = self - money
      return self.balance
  def check_balance(self):
    print(self.balance)
Account_my = input().split()
Account_my_name=Account_my[0]
Account_my_money=Account_my[1]

Account_my = Account(Account_my_name,Account_my_money)
n = int(input())
for i in range(n):
  data = input().split()
  name = data[0]
  money = int(data[1])
  if name == "deposit":
    Account_my.deposit(money)
  elif name == "withdraw":
    Account_my.withdraw(money)

Account_my.check_balance()