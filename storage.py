# This is the storag.py file. Created 2023.12.08
# Author: Victor Magopat
# This file contains the definition for the storage functionality.
# Implements all the interaction between the database and the permanent storage. 

import account
import json

# String definitions for the JSON fields
strAccNo = "account_no"
strAccName = "name"
strAccType = "type"
strAccInterest = "interest"
strAccBalance = "balance"
strAccOverdraftMinBalance = "overdraft_minbalance"

# This is the Storage class. This class is loading and saving the database from/to file.
# Implements the persisten storage using the JSON format and the database.json file.
class Storage:
    # Read the database.json file and return the accounts list
    def ReadDatabase(self):
        with open('database.json', 'r') as file:
            try:
                data_from_file = json.load(file)
            except:
                print("Error: the database.json file contains invalid data.")
                exit()
        
        listLenght = len(data_from_file)

        existingAccounts = []
        index = 0
        while index < listLenght:
            currentAcc = data_from_file[index]
            self.ValidateJsonAcc(currentAcc)
            if ( account.ACC_TYPE_CHEQUING == currentAcc[strAccType]):
                newChequingAcc = account.ChequingAccount()
                newChequingAcc.setAccountHolderName(currentAcc[strAccName])
                newChequingAcc.setAccountNumber(currentAcc[strAccNo])                
                newChequingAcc.setRateOfInterest(currentAcc[strAccInterest])
                newChequingAcc.deposit(currentAcc[strAccBalance])
                newChequingAcc.setOverdraftLimit(currentAcc[strAccOverdraftMinBalance])
                existingAccounts.append(newChequingAcc)
            elif ( account.ACC_TYPE_SAVING == currentAcc[strAccType]):
                newSavingAcc = account.SavingAccount()
                newSavingAcc.setAccountHolderName(currentAcc[strAccName])
                newSavingAcc.setAccountNumber(currentAcc[strAccNo])
                newSavingAcc.setRateOfInterest(currentAcc[strAccInterest])
                newSavingAcc.deposit(currentAcc[strAccBalance])
                newSavingAcc.setMinimumBalance(currentAcc[strAccOverdraftMinBalance])
                existingAccounts.append(newSavingAcc)
            else:
                print("Critical error reading the acc_type in the json file.")
                exit()
            index += 1

        return existingAccounts

    # Write the accounts list to the database.json
    def WriteDatabase(self, allAccounts):
        allJsonAccounts = []
        listLenght = len(allAccounts)
        
        index = 0
        while index < listLenght:
            acc = allAccounts[index]
            acc_no = acc.getAccountNumber()
            acc_name = acc.getAcountHolderName()
            acc_type = acc.getAccountType()
            acc_interest = acc.getRateOfInterest()
            acc_balance = acc.getCurrentBalance()
            if ( account.ACC_TYPE_CHEQUING == acc_type):
                acc_overdraft_minbalance = acc.getOverdraftLimit()
            elif ( account.ACC_TYPE_SAVING == acc_type):
                acc_overdraft_minbalance = acc.getMinimumBalance()
            else:
                print("Critical error reading the acc_type in json file.")
                exit()

            json_acc = {strAccNo: acc_no,
            strAccName: acc_name,
            strAccType: acc_type,
            strAccInterest: acc_interest,
            strAccBalance: acc_balance,
            strAccOverdraftMinBalance: acc_overdraft_minbalance }
            allJsonAccounts.append(json_acc)
            
            index += 1

        with open('database.json', 'w') as file:
            json.dump(allJsonAccounts, file, indent=2)

    # validates the JSON data format
    def ValidateJsonAcc(self, currentAcc):
        try:
            valid = currentAcc[strAccType]
        except:
            print("Error: the database.json file contains invalid type-data.")
            exit()
        try:
            valid = currentAcc[strAccName]
        except:
            print("Error: the database.json file contains invalid name-data.")
            exit()
        try:
            valid = currentAcc[strAccNo]
        except:
            print("Error: the database.json file contains invalid account_no-data.")
            exit()
        try:
            valid = currentAcc[strAccInterest]
        except:
            print("Error: the database.json file contains invalid interest-data.")
            exit()
        try:
            valid = currentAcc[strAccBalance]
        except:
            print("Error: the database.json file contains invalid balance-data.")
            exit()
        try:
            valid = currentAcc[strAccOverdraftMinBalance]
        except:
            print("Error: the database.json file contains invalid overdraft_minbalance-data.")
            exit()


# this code is testing the functionality of the storage module
if __name__ == "__main__":
    print("Testing the storage implementation!")
    
    testStorage = Storage()

    ExistingAccounts = []
    ExistingAccounts = testStorage.ReadDatabase()

    # print the list of the test accounts
    listLenght = len(ExistingAccounts) 
    print("There are :", str(listLenght), "accounts in the test list.")

    myIndex = 0
    while myIndex < listLenght:
        account_name = ExistingAccounts[myIndex].getAcountHolderName()
        print("Account name: ", account_name, "type:", ExistingAccounts[myIndex].getAccountType())
        myIndex += 1
    print("Finished printing the test list.")

    addChequingAcc = account.ChequingAccount()
    addChequingAcc.setAccountHolderName("Saint George")
    addChequingAcc.setAccountNumber(1206)
    addChequingAcc.setRateOfInterest(0.5)
    addChequingAcc.setOverdraftLimit(2003)
    ExistingAccounts.append(addChequingAcc)

    addSavingAcc = account.SavingAccount()
    addSavingAcc.setAccountHolderName("King Arthur")
    addSavingAcc.setAccountNumber(1225)
    addSavingAcc.setRateOfInterest(1.1)
    addSavingAcc.setMinimumBalance(522)
    ExistingAccounts.append(addSavingAcc)

    listLenght = len(ExistingAccounts) 
    print("There are :", str(listLenght), "accounts in the new list.")

    myIndex = 0
    while myIndex < listLenght:
        account_name = ExistingAccounts[myIndex].getAcountHolderName()
        print("Account name: ", account_name, "type:", ExistingAccounts[myIndex].getAccountType())
        myIndex += 1
    print("Finished printing the new list.")

    testStorage.WriteDatabase(ExistingAccounts)

    exit()