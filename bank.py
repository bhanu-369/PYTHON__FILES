class BankAccount:
    def __init__(self,account_holder,balance=0):
         self.account_holder=account_holder
         self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return f"${amount} deposited.Current balance:${self.balance}"
        
    def withdraw(self,amount):
        if amount>=self.balance:
            return "insufficient balance"
        self.balance-=amount
        return f"${amount} withdrawn ,current balance:${self.balance}"
    def checkbalance(self):
       return f"Account holder:{self.account_holder},balance:${self.balance}"
accounts=BankAccount("Deepa",10000)
print(accounts.deposit(50))
print(accounts.withdraw(1000))
print(accounts.checkbalance())
print(accounts.withdraw(1000))

    
