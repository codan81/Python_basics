"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Withdrawal Dialog.
    
    arfgs:
          account(dict) 
    return:
        account(dict): returns account with balance adjusted for withdrawal
    
    """

    # @TODO:  Use questionary to capture the withdrawal and set it equal to amount variable. Be sure that amount is a floating point number.
    withdrawal_amount = questionary.text("How much you would like to withdrawal?").ask()
    withdrawal_amount = float(withdrawal_amount)

    # @TODO:  Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if withdrawal_amount <= 0.0:
        sys.exit(f"you should input a correct amount")

    # @TODO: Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    if withdrawal_amount <= account["balance"]:
        account["balance"] = account["balance"] - withdrawal_amount
        print (f"transaction succesful!")
        return account
    else:
        sys.exit(f"you don't have sufficient funds to realize this withdrawal")

    