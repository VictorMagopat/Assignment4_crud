# This is the storag.py file. Created 2023.12.08
# Author: Victor Magopat
# This file contains the definition for the storage functionality.
# Implements all the interaction between the database and the permanent storage. 

import account
import json

# Read the database.json file and store the data in a variable
def ReadDatabase():
    with open('database.json', 'r') as file:
        data_from_file = json.load(file)
    
    listLenght = len(data_from_file)

    newSavingAcc = account.SavingAccount()
    newChequingAcc = account.ChequingAccount()

    existingAccounts = []
    index = 0
    while index < listLenght:
        currentAcc = data_from_file[index]
        if ( 1 == currentAcc['type']):
            newChequingAcc.setAccountHolderName(currentAcc['name'])
            newChequingAcc.setAccountNumber(currentAcc['account_no'])
            newChequingAcc.setRateOfInterest(currentAcc['interest'])
            newChequingAcc.setOverdraftLimit(currentAcc['overdraft_minbalance'])
            existingAccounts.append(newChequingAcc)
        if ( 2 == currentAcc['type']):
            newSavingAcc.setAccountHolderName(currentAcc['name'])
            newSavingAcc.setAccountNumber(currentAcc['account_no'])
            newSavingAcc.setRateOfInterest(currentAcc['interest'])
            newSavingAcc.setMinimumBalance(currentAcc['overdraft_minbalance'])
            existingAccounts.append(newSavingAcc)
        index += 1

    return existingAccounts

def WriteDatabase(allAccounts):
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
        if ( 1 == acc_type):
            acc_overdraft_minbalance = acc.getOverdraftLimit()
        if ( 2 == acc_type):
            acc_overdraft_minbalance = acc.getMinimumBalance()

        json_acc = {"account_no": acc_no,
        "name": acc_name,
        "type": acc_type,
        "interest": acc_interest,
        "balance": acc_balance,
        "overdraft_minbalance": acc_overdraft_minbalance }
        allJsonAccounts.append(json_acc)
        
        index += 1

    with open('database.json', 'w') as file:
        json.dump(allJsonAccounts, file, indent=2)



# this code is testing the functionality of the storage module
if __name__ == "__main__":
    print("Testing the storage implementation!")
    
    ExistingAccounts = []
    ExistingAccounts = ReadDatabase()

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
    addChequingAcc.setAccountHolderName("Saint Nicholas")
    addChequingAcc.setAccountNumber(1206)
    addChequingAcc.setRateOfInterest(0.5)
    addChequingAcc.setOverdraftLimit(2003)
    ExistingAccounts.append(addChequingAcc)

    addSavingAcc = account.SavingAccount()
    addSavingAcc.setAccountHolderName("Kris Kringle")
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

    WriteDatabase(ExistingAccounts)

    exit()