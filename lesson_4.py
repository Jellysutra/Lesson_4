class BankAccount:
    bank_name = "Bank of Python"

    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def welcome(self):
        print("Welcome,", self.account_holder_name, "!")

    # Here is a getter for the balance attribute
    def check_balance(self):
        return self.balance

	# Here is a setter for the balance
    def deposit(self, amount):
        self.balance += amount
    
    # Here is a setter (withdrawal) for the balance
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance -= amount

darren_account = BankAccount('Darren', 123456789, 1000)
darren_account.deposit(5000)
print(darren_account.check_balance()) # 6000

darren_account.withdraw(5000)
print(darren_account.check_balance()) # 1000

darren_account.withdraw(5000) # error