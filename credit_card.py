class CreditCard:

    def __init__(self, account_number, credit_limit):
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.balance = 0
    
    # To check balance
    def get_balance(self):
        return self.balance
    
     # To check balance
    def get_credit_limit(self):
        return self.credit_limit
    
    # To set the credit limit
    def set_credit_limit(self, amount):
        if amount > 100000 or amount < 0:
            print("Above limit!")       
        else:
            self.credit_limit = amount

    # To make a purcharse
    def make_purchase(self, amount):
        if amount < 0  or amount > (self.credit_limit-self.balance):
            print("Invalid Transaction")
        else:
            self.balance += amount

    # To make payment 
    def make_payment(self,amount):
        if amount < 0 :
            print("Invalid Transaction")
        elif amount > self.balance:
             self.balance = 0
        else:
            self.balance -= amount
    
    # report method
    def report(self):
        print(f"Account number: {self.account_number}, Balance: ${self.balance}")


class RewardsCard(CreditCard): # inherits from CreditCard
    def __init__(self, account_number, credit_limit, rewards_rate):
        # call the superclass initialiser
        super().__init__(account_number,credit_limit)
        # add the rewards_rate attribute
        self.rewards_rate = rewards_rate
        self.balance = 0
        self.rewards_pt = 0
    
    def check_rewards(self):
        return self.rewards_pt

    def accumulate_rewards(self, amount):
        self.rewards_pt += amount*self.rewards_rate/100
    
    def redeem_rewards(self, amount):
        self.rewards_pt -= amount
    
    def make_purchase(self, amount):
        if amount < 0  or amount > (self.credit_limit-self.balance):
            print("Invalid Transaction")
        else:
            self.rewards_pt += amount
            self.balance += amount
    
    def report(self):
        print(f"Account number: {self.account_number}, Balance: ${self.balance}, Rewards: {self.rewards_pt}")

class CashbackCard(CreditCard): # inherits from CreditCard
    def __init__(self, account_number, credit_limit, cash_back):
        # call the superclass initialiser
        super().__init__(account_number,credit_limit)
        # add the cash_back attribute
        self.cash_back = cash_back
        self.cb_earned = 0
    
    def make_purchase(self, amount):
        if amount < 0  or amount > (self.credit_limit-self.balance):
            print("Invalid Transaction")
        else:
            self.balance += amount
            self.cb_earned += amount*self.cash_back/100
            self.balance -= self.cb_earned
    
    def report(self):
        print(f"Account number: {self.account_number}, Balance: ${self.balance}, Cashback Earn: {self.cb_earned}")
        

my_credit_card = CreditCard(123456789, 5000)
assert my_credit_card.account_number == 123456789
assert my_credit_card.get_balance() == 0
assert my_credit_card.get_credit_limit() == 5000

my_credit_card.set_credit_limit(1000)
my_credit_card.set_credit_limit(-1)       # print error
my_credit_card.set_credit_limit(100001)   # print error
assert my_credit_card.get_credit_limit() == 1000

my_credit_card.make_purchase(900)
my_credit_card.make_purchase(-1)          # print error
my_credit_card.make_purchase(200)         # print error
assert my_credit_card.get_balance() == 900

my_credit_card.make_payment(500)
assert my_credit_card.get_balance() == 400

my_credit_card.make_payment(5000)
assert my_credit_card.get_balance() == 0

print("All tests passed!")

my_rewards_card = RewardsCard(12345678, 5000, 2)
my_cashback_card = CashbackCard(11111, 5000, 2)

my_rewards_card.make_purchase(900)
my_rewards_card.make_purchase(1900)
my_cashback_card.make_purchase(900)
my_cashback_card.make_purchase(900)


print(my_rewards_card.get_balance())
print(my_cashback_card.get_balance())

my_cashback_card.report()
my_rewards_card.report()