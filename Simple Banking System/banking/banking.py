import account
import bank_system
import bank_db


bank = bank_system.BankSystem()
db = bank_db.BankDB()

bank.choice()

while bank.user_choice != "0":

    # 1. Create an account
    if bank.state == 'logout' and bank.user_choice == "1":
        db.insertCard(bank.accountCreate())
        bank.user_choice = ''

    # 2. Log into account
    if bank.state == 'logout' and bank.user_choice == "2":
        card = input("Enter your card number:\n")
        pin = input("Enter your PIN:\n")
        acc_id = db.checkAcc(card, pin)
        if acc_id != -1:
            bank.accountLogin(acc_id)
        else:
            print("Wrong card number or PIN!")
        bank.user_choice = ''

    # 1. Balance
    if bank.state == 'login' and bank.user_choice == "1":
        balance = db.checkBalance(bank.active_acc_id)
        print("\nBalance: ", balance)
        bank.user_choice = ''

    # 2. Add income
    if bank.state == 'login' and bank.user_choice == "2":
        income = int(input("Enter income:"))
        db.addIncome(bank.active_acc_id, income)
        print("Income was added!")
        bank.user_choice = ''

    # 3. Do transfer
    if bank.state == 'login' and bank.user_choice == "3":
        receiver_id = ''
        money = 0
        is_error = 0
        receiver = input("Enter card number:")

        if account.BankAccount.luhnAlgorithm(receiver) == 0:
            print("Probably you made a mistake in the card number. Please try again!")
            is_error = 1

        if is_error == 0:
            receiver_id = db.checkCard(receiver)
            if receiver_id == -1:
                print("Such a card does not exist.")
                is_error = 1

        if is_error == 0:
            money = int(input("Enter how much money you want to transfer:"))
            balance = db.checkBalance(bank.active_acc_id)
            if money > int(balance):
                print("Not enough money!")
                is_error = 1

        if is_error == 0:
            db.addIncome(bank.active_acc_id, -money)
            db.addIncome(receiver_id, money)
            print("Success!")

        bank.user_choice = ''

    # 4. Close account
    if bank.state == 'login' and bank.user_choice == "4":
        db.deleteAcc(bank.active_acc_id)
        bank.active_acc_id = -1
        bank.user_choice = ''

    # 5. Log out
    if bank.state == 'login' and bank.user_choice == "5":
        bank.active_acc_index = -1
        bank.state = 'logout'
        print("You have successfully logged out!")
        bank.user_choice = ''

    bank.choice()

print("Bye!")
