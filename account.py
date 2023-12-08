# This is the account.py file. Created 2023.11.08
# Author: Victor Magopat
# This file contains the definition for:
# - class Account, generic account 
# - class SavingsAccount, Account with specifics for Savings
# - class ChequingAccount, Account wiht specifics for Chequing 

# definitions for the account type
ACC_TYPE_GENERIC = 0
ACC_TYPE_CHEQUING = 1
ACC_TYPE_SAVING = 2

# definition for the transactions
TRANSACTION_PROCESSED = True
TRANSACTION_FAILED = False

# definition of class Account, the base for classes SavingsAccount and ChequingAccount.
class Account():

    def __init__(self) -> None:
        pass
    __accountType: int
    __accountNumber: int
    __accountHolderName: str
    __rateOfInterest: float
    __currentBalance: float

    __accountType = ACC_TYPE_GENERIC
    __accountNumber = 999999999
    __accountHolderName = "NOT DEFINED"
    __rateOfInterest = 0
    __currentBalance = 0

    # returns the accountNumber 
    def getAccountNumber(self):
        return self.__accountNumber

    # returns the AccountHolderName
    def getAcountHolderName(self):
        return self.__accountHolderName

    # returns the rateOfInterest
    def getRateOfInterest(self):
        return self.__rateOfInterest

    # returns the 
    def getCurrentBalance(self):
        return self.__currentBalance
    
    # returns the type of the account
    def getAccountType(self):
        return self.__accountType

    # sets the accountHolderName
    def setAccountNumber(self, NewAccountNumber):
        self.__accountNumber = NewAccountNumber

    # sets the accountHolderName
    def setAccountHolderName(self, NewAccountName):
        self.__accountHolderName = NewAccountName

    # sets the rateOfInterest
    def setRateOfInterest(self, NewRateOfInterest):
        self.__rateOfInterest = NewRateOfInterest
    
    # sets the type of the account
    def setAccountType(self, NewAccountType) :
        self.__accountType = NewAccountType

    # adds the DepositSum to the currentBalance
    def deposit(self, DepositSum):
        self.__currentBalance += DepositSum

    # subtracts the WithdrawSum from the current Balance
    # reject transactions that have sufficient funds
    def withdraw(self, WithdrawSum):
        #if  self.__currentBalance >= WithdrawSum:           
        self.__currentBalance -= WithdrawSum
        return TRANSACTION_PROCESSED
        #else:
        #    return TRANSACTION_FAILED



# definition of the ChequingAccount class. This account allows overdrafts,
# the account holder can withdraw an amount that is more than their current balance.
class ChequingAccount(Account):

    def __init__(self) -> None:
        self.setAccountType(ACC_TYPE_CHEQUING)
        pass

    #__accountType = ACC_TYPE_CHEQUING
        
    __overdraftLimit: float
    __overdraftTransactions: int
    __overdraftLimit = 500
    __overdraftTransactions = 0

    def setOverdraftLimit(self, NewOverdraftLimit):
        self.__overdraftLimit = NewOverdraftLimit

    def getOverdraftLimit(self):
        return self.__overdraftLimit

    # override the method withdraw of the base class to reject transactions that cannot be 
    # completed even after using the overdraft limit. This means if an account has an overdraft
    # limit of 5000 CAD, the account holder is allowed to withdraw up to 5000 CAD more than the 
    # money they have in the account.
    def withdraw(self, WithdrawSum):
        balance = self.getCurrentBalance()
        if ( balance>= WithdrawSum):
            super(ChequingAccount, self).withdraw(WithdrawSum)
            return TRANSACTION_PROCESSED
        elif (balance + self.__overdraftLimit) >= WithdrawSum:
            super(ChequingAccount, self).withdraw(WithdrawSum)
            self.__overdraftTransactions += 1
            return TRANSACTION_PROCESSED
        else:
            return TRANSACTION_FAILED


# definition of the SavingAccount class. This account requires the account holder
# to maintain a minimum balance in the account.
class SavingAccount(Account):

    def __init__(self) -> None:
        self.setAccountType(ACC_TYPE_SAVING)
        pass
    __minimumBalance: float
    __minimumBalance = 1000

    def setMinimumBalance(self, NewMinBalance):
        self.__minimumBalance = NewMinBalance

    def getMinimumBalance(self):
        return self.__minimumBalance

    # override the method withdraw of the base class to reject the transactions that would bring 
    # the current balance of the account below the minimum balance. E.g., if the minimum balance 
    # is 5000 CAD and the current balance in the account is 7000 CAD, the maximum withdrawal that
    # can be allowed is 2000 CAD.
    def withdraw(self, WithdrawSum):        
        balance = self.getCurrentBalance()        
        if balance >= (WithdrawSum + self.__minimumBalance):
            #self.__currentBalance -= WithdrawSum
            super(SavingAccount, self).withdraw(WithdrawSum)
            return TRANSACTION_PROCESSED
        else:
            return TRANSACTION_FAILED


# this code is testing the functionality of the account module
if __name__ == "__main__":
    print("Testing the account implementation!")

    # print the account information
    def PrintAccountInfo(acc):
        accNo = acc.getAccountNumber()
        accName = acc.getAcountHolderName()
        accRate = acc.getRateOfInterest()
        accBal = acc.getCurrentBalance()
        accType = acc.getAccountType()
        print("Account information:")
        print("        Name: ", accName)
        print("        Number: ", str(accNo))
        print("        Balance: ", str(accBal))
        print("        Interest Rate: ", str(accRate))
        if ACC_TYPE_GENERIC == accType:
            print("        Type: Generic")
        elif ACC_TYPE_CHEQUING == accType:
            print("        Type: Chequing Account")
            overDraft = acc.getOverdraftLimit()
            print("        Overdraft Limit: ", str(overDraft))
        elif ACC_TYPE_SAVING == accType:
            print("        Type: Saving Account")
            minBal = acc.getMinimumBalance()
            print("        Minimum Balance: ", str(minBal))
        else:
            print("        Type: Unknown")
    
    # instantiate a generic account and print the defaults
    GenAcc = Account()
    #PrintAccountInfo(GenAcc)

    # set the attributes of the generic account
    GenAcc.setAccountHolderName("John North")
    GenAcc.setAccountNumber(123456789)
    GenAcc.setRateOfInterest("0.01")
    GenAcc.deposit(201.45)
    PrintAccountInfo(GenAcc)

    # instantiate a saving account and print the defaults
    SaveAcc = SavingAccount()
    #PrintAccountInfo(SaveAcc)

    # set the attributes of the saving account
    SaveAcc.setAccountHolderName("Mike South")
    SaveAcc.setAccountNumber(987654321)
    SaveAcc.setRateOfInterest("0.1")
    SaveAcc.deposit(625.81)
    SaveAcc.setMinimumBalance(100)
    PrintAccountInfo(SaveAcc)

   # instantiate a chequing account and print the defaults
    CheqAcc = ChequingAccount()
    #PrintAccountInfo(SaveAcc)

    # set the attributes of the chequing account
    CheqAcc.setAccountHolderName("Tom West")
    CheqAcc.setAccountNumber(6543210987)
    CheqAcc.setRateOfInterest("0.01")
    CheqAcc.deposit(144.09)
    CheqAcc.setOverdraftLimit(500)
    PrintAccountInfo(CheqAcc)

    # test the overdraft in the ChequingAccount
    balance_available = 0
    withdraw_sum  = 50
    transaction_summary = ""
    you_have_money = True
    while you_have_money == True:
        balance_available = CheqAcc.getCurrentBalance()
        transaction_summary = "You have " + str(balance_available)
        you_have_money = CheqAcc.withdraw(withdraw_sum)
        transaction_summary += " withdraw: " + str(withdraw_sum)
        if you_have_money == True:
            transaction_summary += " balance available" + str(CheqAcc.getCurrentBalance())
        else:
            transaction_summary += " balance available" + str(CheqAcc.getCurrentBalance())
            transaction_summary += " insufficient funds!"
        print(transaction_summary)

    print("Chequing Account: test complete!")

    # test the minimum limit in the SavingAccount
    you_have_money = True
    while you_have_money == True:
        balance_available = SaveAcc.getCurrentBalance()
        transaction_summary = "You have " + str(balance_available)
        you_have_money = SaveAcc.withdraw(withdraw_sum)
        transaction_summary += " withdraw: " + str(withdraw_sum)
        if you_have_money == True:
            transaction_summary += " balance available " + str(SaveAcc.getCurrentBalance())
        else:
            transaction_summary += " balance available " + str(SaveAcc.getCurrentBalance())
            transaction_summary += " insufficient funds!"
        print(transaction_summary)

    print("Saving Account: test complete!")


