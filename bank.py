# This is the bank.py file. Created 2023.11.08
# Author: Victor Magopat
# This file contains the definition for the Bank class

import account
import storage 
    
# predefined Saving accounts
Acc_01 = account.SavingAccount()
Acc_01.setAccountHolderName("Tom West")
Acc_01.setAccountNumber(1)
Acc_02 = account.SavingAccount()
Acc_02.setAccountHolderName("John North")
Acc_02.setAccountNumber(2)
Acc_03 = account.SavingAccount()
Acc_03.setAccountHolderName("Mike South")
Acc_03.setAccountNumber(3)

# predefined Chequing accounts
Acc_04 = account.ChequingAccount()
Acc_04.setAccountHolderName("Sarah West")
Acc_04.setAccountNumber(4)
Acc_05 = account.ChequingAccount()
Acc_05.setAccountHolderName("Anne North")
Acc_05.setAccountNumber(5)
Acc_06 = account.ChequingAccount()
Acc_06.setAccountHolderName("Jane South")
Acc_06.setAccountNumber(6)

ExistingAccounts = [Acc_01, Acc_02, Acc_03, Acc_04, Acc_05, Acc_06]


class Bank:
    def __init__(self, existingAccounts = [], lastAccountNumber = 0, bankName = "Famous Bank") -> None:
        
        # this keeps track of all the accounts
        self.lastAccountNumber: int  
        # this is the name of the Bank 
        self.bankName: str

        self.lastAccountNumber = lastAccountNumber
        self.bankName = bankName

        # Define a constructor that populates the account list with hardcoded of three 
        # ChequingAccount instances and three SavingsAccount instances. 
        listLenght = len(existingAccounts)
        self.lastAccountNumber = listLenght 
        index = 0
        while index < listLenght:
            self.databaseAcc.append(existingAccounts[index])
            index += 1
        pass

    # the bank class has a List of Account objects
    databaseAcc = []
    lastAccountNumber = 0

    # method that populates the account list with data from json file
    def openDatabase(self):
        self.databaseAcc.clear()
        self.databaseAcc = storage.ReadDatabase()
        listLenght = len(self.databaseAcc)
        self.lastAccountNumber = listLenght
        pass
    
    # method that writes the account list to the json file
    def writeDatabase(self):        
        storage.WriteDatabase(self.databaseAcc)
        pass

    # return the number of accounts
    def getLastAccountNumber(self):
        listLenght = len(self.databaseAcc)
        self.lastAccountNumber = listLenght 
        return self.lastAccountNumber
    
    # removes the account at index accNo; return -1 if failed
    # or the total no of accounts
    def deleteAccountNumber(self, accNo):
        opComplete = -1
        listLenght = len(self.databaseAcc)
        if (accNo > listLenght):
            opComplete = -1
        else:
            self.databaseAcc.pop(accNo)
            listLenght = len(self.databaseAcc)
            self.lastAccountNumber = listLenght
            opComplete = listLenght
        return opComplete

    # instantiates a saving account and appends it to the list
    def openAccountSaving(self, holderName: str):
        openNewAcc = account.SavingAccount()
        openNewAcc.setAccountHolderName(holderName)
        
        self.lastAccountNumber = len(self.databaseAcc) + 1
        openNewAcc.setAccountNumber(self.lastAccountNumber + 100)
        
        self.databaseAcc.append(openNewAcc)        
        pass

    # instantiates a checking account and appends it to the list
    def openAccountChequing(self, holderName: str):
        openNewAcc = account.ChequingAccount()
        openNewAcc.setAccountHolderName(holderName)
        
        self.lastAccountNumber = len(self.databaseAcc) + 1
        openNewAcc.setAccountNumber(self.lastAccountNumber + 100)

        self.databaseAcc.append(openNewAcc)
        pass
    
    # search database by account number. Returns the index of the account or "-1"
    def searchAccountByNo(self, accNo, accType):
        # accFound is the index of the account or "-1" for not found.
        accFound = -1
        currType = 0
        accIndex = 0
        while accIndex < self.lastAccountNumber:
            currAcc = self.databaseAcc[accIndex].getAccountNumber()
            currType = self.databaseAcc[accIndex].getAccountType()
            if (accNo == currAcc) and (accType == currType):
                accFound = accIndex
                break
            else:
                accFound = -1
            accIndex += 1
        return accFound        

    # search database by account name. Returns the index of the account or "-1"
    def searchAccountByName(self, accName, accType):        
        # accFound is the index of the account or "-1" for not found.
        accFound = -1
        currType = 0 
        accIndex = 0
        while accIndex < self.lastAccountNumber:
            currName = self.databaseAcc[accIndex].getAcountHolderName()
            currType = self.databaseAcc[accIndex].getAccountType()
            if (accName == currName) and (accType == currType):
                accFound = accIndex
                break
            else:
                accFound = -1
            accIndex += 1
        return accFound


# this code is testing the functionality of the bank module
if __name__ == "__main__":

    print("Testing the bank implementation!")

    # init_mode = 1 initialize using the hardcoded values
    # init_mode = 2 initialize using database.json
    init_mode = 2
    if ( 1 == init_mode):
        # print the list of the test accounts
        listLenght = len(ExistingAccounts) 
        print("There are :", str(listLenght), "accounts in the test list.")

        myIndex = 0
        while myIndex < listLenght:
            account_name = ExistingAccounts[myIndex].getAcountHolderName()
            print("Account name: ", account_name, "type:", ExistingAccounts[myIndex].getAccountType())
            myIndex += 1
        print("Finished printing the test list.")

        # initialize the bank account
        myBank = Bank(ExistingAccounts)
    elif ( 2 == init_mode):
        myBank = Bank()
        myBank.openDatabase()
    else:
        print("Critical failure in testing the bank module")
        exit()

    noOfAccounts = myBank.getLastAccountNumber() #Bank.lastAccountNumber 
    print("Last account number is: ", str(noOfAccounts))
    nameOfBank = myBank.bankName
    print("Bank name is: ", nameOfBank )

    myIndex = 0
    while myIndex < myBank.lastAccountNumber:
        account_name = myBank.databaseAcc[myIndex].getAcountHolderName()
        account_no = myBank.databaseAcc[myIndex].getAccountNumber()
        account_type = myBank.databaseAcc[myIndex].getAccountType()
        print("Account name: ", account_name, "Account number: ", str(account_no), " type: ", str(account_type))
        myIndex += 1
    print("Finished printing the bank list.")

    if ( 1 == init_mode):
        searchAccNo = 5
        print("Search by Account Number")
        foundAcc = myBank.searchAccountByNo(searchAccNo, account.ACC_TYPE_SAVING)
        if foundAcc < 0:
            print("The Saving account number", str(searchAccNo), "does't exist")
        else:
            print("Found Saving account number: ", str(searchAccNo))    

        foundAcc = myBank.searchAccountByNo(searchAccNo, account.ACC_TYPE_CHEQUING)
        if foundAcc < 0:
            print("The Chequing account number", str(searchAccNo), "does't exist")
        else:
            print("Found Chequing account number: ", str(searchAccNo))      

        searchAccName = "Anne North"
        print("Search by Account Name")
        foundAcc = myBank.searchAccountByName(searchAccName, account.ACC_TYPE_SAVING)
        if foundAcc < 0:
            print("There is no Saving account with the name", searchAccName, ". It does't exist.")
        else:
            print("Found Saving account: ", searchAccName, "with account number", str(foundAcc))

        print("Search by Account Name")
        foundAcc = myBank.searchAccountByName(searchAccName, account.ACC_TYPE_CHEQUING)
        if foundAcc < 0:
            print("There is no Chequing account with the name", searchAccName, ". It does't exist.")
        else:
            print("Found Chequing account: ", searchAccName, "with account number", str(foundAcc))

    newAccHolderName = "Nora East"
    print("Create new Chequing Account for: ", newAccHolderName)
    myBank.openAccountChequing(newAccHolderName)

    newAccHolderName = "Rick East"
    print("Create new Saving Account for: ", newAccHolderName)
    myBank.openAccountSaving(newAccHolderName)

    myIndex = 0
    while myIndex < myBank.getLastAccountNumber():
        account_name = myBank.databaseAcc[myIndex].getAcountHolderName()
        account_no = myBank.databaseAcc[myIndex].getAccountNumber()
        print("Account name: ", account_name, "Account number: ", str(account_no))
        myIndex += 1
    print("Finished printing the updated bank list.")

    if ( 1 == init_mode):
        print("There is nothing to save to file")
    elif (2 == init_mode):
        myBank.writeDatabase()
        print("Data was saved succesfully saved to file.")
    else:
        print("Critical failure in testing the bank module")
    
    exit()