"""This is a basic ATM Application.

This is a program consists of the basic actions of an ATM.

Example:
    $ python app.py
"""

accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3278.42}
]

# Create the `login` function for the ATM application.
# The login function will take in a user PIN.
# The function should validate the PIN against this list of `accounts`.
# If the PIN is validated, the function should return the account's balance.

def login(pin):
    for account in accounts:
        if int(pin) == account["pin"]:
            account_balance = account['balance']

    return account_balance

# Create the `check_balance` function for the ATM application.
# Once the pin number is inputed, and if everything is ok the user will be able to check his/her balance
# the check balance function should return the current balance of the account

def check_balance(account_balance):
    print(f"the balance in your account is: $ {account_balance}.")



# Create the `make_deposit` function for the ATM application.
# The function should take in the account balance and deposit amount as parameters.
# The function should validate that the deposit amount is greater than 0.
# The deposit balance should equal the account balance plus the deposit amount.
# The function should return the balance after being adjusted for the deposit.

def make_deposit(account_balance, deposit):
    if deposit > 0:
        deposit_balance = account_balance + deposit
        print(f"the new balance of your account is:${deposit}.")
    else:
        print("your deposit amount must be positive")
    return(deposit_balance)



# Create the `make_withdrawal` function for the ATM application.
# The function should take in the account balance and withdrawal amount as parameters.
# The function should validate that the account balance is greater than the withdrawal.
# The withdrawal balance should equal the account balance minus the withdrawal amount.
# The function should return the account balance after being adjusted for the withdrawal.

def make_withdrawl(account_balance, withdrawal):
    if account_balance > withdrawal:
        withdrawal_balance = account_balance - withdrawal
        print(f'The new Balance of your account is: ${withdrawal_balance}.')
    else: 
        print("You do not have the funds to make this withdrawal.")
    return(withdrawal_balance)