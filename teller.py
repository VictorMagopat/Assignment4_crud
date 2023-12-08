# This is the teller.py file. Created 2023.11.08
# Author: Victor Magopat
# This file contains the definition for the class Application.
# Implements all the interaction between the user and the Bank. 
# No other class is allowed to interact (input or print) with the end user. 

import account
import bank

# this is the welcome string
WelcomeMessage = "Welcome to Famous Bank.\n"

# this is the goodbye message
GoodbyeMessage = "Have a nice day.\nGoodbye!"

# this is the main menu 
OptionsMainMenu = """Bank main menu options:
            <1> Select Chequing Account
            <2> Select Saving Account
            <3> Open Account
            <4> Exit"""

# this is the main menu 
AccountSearchMenu = """Search options:
            <1> Search Account by <Number>
            <2> Search Account by <Name>
            <3> Return to main menu"""

# This is the account menu 
AccountOperationsMenu = """Account menu:
            <1> Check Balance
            <2> Deposit
            <3> Withdraw
            <4> Return to main menu"""

# Account type menu
AccountTypeMenu = """What account type would like to open:
            <1> Saving Account  
            <2> Chequing Account\n"""


# This is the Application class. This class is what the user interacts with to access the bank
# and the accounts attached to thier bank. This class holds all menus calls all methods from the
# bank class.
class Application:

    # initialize the bank database
    famousBank = bank.Bank(bank.ExistingAccounts)

    # the account index that is served now
    serveAccIndex = int(0)    

    # Define and call the method run() to show the main menu to the end user.
    # Try creating methods to implement functionality for each menu option other than exit.
    def run(self):
        print(WelcomeMessage)

        self.showMainMenu()

        print(GoodbyeMessage)
        pass


	# The showMainMenu method displays the following options until the user chooses to exit:
    # 1. Select Account: this allows the user to enter the account number of the account they
    #    want to work with. Upon searching the account successfully, the application will call
    #    the method showAccountMenu to display the Account Menu as described next.
    # 2. Open Account: allows the user to open a new account *To be implemented for Bonus
    # 3. Exit: allows the user to exit the application
    def showMainMenu(self):
        tellerOn = True
        accType = 0
        while tellerOn == True:
            print(OptionsMainMenu)
            menu_start = input("What is your selection: ")

            # search account
            if (menu_start == "1") or (menu_start == "2"):
                if(menu_start == "1"):
                    print("You are looking for a Chequing Account: ")
                    accType = account.ACC_TYPE_CHEQUING
                else:
                    print("You are looking for a Saving Account: ")
                    accType = account.ACC_TYPE_SAVING 
                searchOn = True
                while searchOn == True:
                    print(AccountSearchMenu)
                    menu_start = input("What is your selection: ")

                    # search account by number
                    if menu_start == "1":
                        while True:
                            print("Select account by <Number>: ")
                            accInput = input("Please enter the number of the account: \n")
                            validInput = accInput.isnumeric()
                            if validInput == True:
                                accNo = int(accInput)
                                print("Searching for account number: ", str(accNo))
                                self.serveAccIndex = self.famousBank.searchAccountByNo(accNo, accType)
                                if self.serveAccIndex < 0:
                                    print("This account doesnt exist")
                                    break
                                else:
                                    self.showAccountMenu()
                            else: print("please input a valid number")

                    
                    # search account by name
                    elif menu_start == "2":
                        print("Select account by <Name> ")
                        accName = input("Please enter the name of the account: \n")
                        self.serveAccIndex = self.famousBank.searchAccountByName(accName, accType)
                        print("Searching for account name: ", accName)
                        if self.serveAccIndex < 0:
                            print("This account doesnt exist")
                        else:
                            self.showAccountMenu()

                    # return to main menu
                    elif menu_start == "3":
                        print("You selected return to main menu")
                        searchOn = False
                    elif menu_start == "q":
                        print(GoodbyeMessage)
                        exit()
                    else:
                        print("Please enter: <1>, <2> or <3>") 

            elif menu_start == "3":
                print("Opening a new account.")
                self.showOpenAccountMenu()
                
            elif menu_start == "4":
                print("Exit")
                tellerOn = False

            elif menu_start == "q":
                print(GoodbyeMessage)
                exit()
            else:
                print("Please enter: <1>, <2>, <3> or <4>") 
        pass


    # The showAccountMenu method displays the following options until the user chooses to exit:
    # 1. Check Balance: Display the balance of the selected account
    # 2. Deposit: Prompt the user for an amount to deposit and perform the deposit using the
    #    methods in account class. 
    # 3. Withdraw: Prompt the user for an amount to withdraw and perform the withdrawal using
    #    the methods in the account class. 
    # 4. Exit Account: go back to Banking Main Menu
    def showAccountMenu(self):
        servingAccount = True
        while servingAccount == True:
            print(AccountOperationsMenu)
            menu_start = input("What is your selection: ")

            # print the current balance
            if menu_start == "1":                
                balance = self.famousBank.databaseAcc[self.serveAccIndex].getCurrentBalance()
                print("Your account has a balance of: ", str(balance))

            # process the deposit operation
            elif menu_start == "2":
                deposit = 0
                while True:
                    print("What amount would you like to deposit?")
                    inputSum = input()
                    try:
                        deposit = float(inputSum)
                        if (deposit < 0):
                            print("This is invalid. Please enter a valid number.")
                        else:
                            break
                    except ValueError:
                        print("This is invalid. Please enter a valid number.")

                deposit = round(deposit, 2)
                self.famousBank.databaseAcc[self.serveAccIndex].deposit(deposit)
                print("You deposited: ", str(deposit))
                balance = self.famousBank.databaseAcc[self.serveAccIndex].getCurrentBalance()
                print("Your account has a new balance of: ", str(balance))

            # process the withdraw operation
            elif menu_start == "3":
                withdraw = 0
                while True:
                    print("What amount would you like to withdraw?")
                    inputSum = input()
                    try:
                        withdraw = float(inputSum)
                        if (withdraw < 0):
                            print("This is invalid. Please enter a valid number.")
                        else:
                            break
                    except ValueError:
                        print("This is invalid. Please enter a valid number.")

                withdraw = round(withdraw, 2)
                print("The sum ", str(withdraw), "will be withdrawn from account ", str(self.serveAccIndex))
                transaction = False
                print("You withdraw: ", str(withdraw))

                transaction = self.famousBank.databaseAcc[self.serveAccIndex].withdraw(withdraw)
                if (transaction == account.TRANSACTION_FAILED):
                    print("This transaction failed.")
                else:
                    balance = self.famousBank.databaseAcc[self.serveAccIndex].getCurrentBalance()
                    print("Your account has a new balance of: ", str(balance))

            # return to main menu
            elif menu_start == "4":
                print("You selected to return to main menu")
                servingAccount = False
                
            elif menu_start == "q":
                print(GoodbyeMessage)
                exit()
            else:
                print("Please enter: <1>, <2>, <3> or <4>") 
        pass

    def showOpenAccountMenu(self):
        print("What name is on the new account? ")
        accName = input("Name: ")
        accType = 0
        while True:
            accType = input(AccountTypeMenu)
            if accType == "1":
                self.famousBank.openAccountSaving(accName)
                print("Congratulation", accName, "! Your Savingng Account is opened!")
                break  
            elif accType == "2":                
                self.famousBank.openAccountChequing(accName)
                print("Congratulation", accName, "! Your Chequing Account is opened!")
                break
            elif accType == "q":
                print(GoodbyeMessage)
                exit()
            else:
                print("  Please enter: <1> or <2>") 
        pass



# instantiate and run the application
TellerApp = Application()
TellerApp.run()
