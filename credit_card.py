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
    
    
## Uncomment all lines to test your class once completed

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