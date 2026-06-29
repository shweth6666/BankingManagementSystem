from customer import Customer
from savings_account import SavingsAccount
from current_account import CurrentAccount
from bank import Bank

bank = Bank()
current_customer = None

while True:

    print("\n===== BANKING MANAGEMENT SYSTEM =====")
    print("1. Register Customer")
    print("2. Create Savings Account")
    print("3. Create Current Account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Check Balance")
    print("7. Transaction History")
    print("8. Calculate Interest")
    print("9. Search Customer")
    print("10. Account Statement")
    print("11. Fund Transfer")
    print("12. Apply Service Charge")
    print("13. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        cid = input("Customer ID: ")
        name = input("Customer Name: ")

        customer = Customer(cid, name)

        bank.add_customer(customer)

        current_customer = customer

        print("Customer Registered Successfully")

    elif choice == "2":

        if current_customer:

            acc_no = input("Account Number: ")

            current_customer.account = SavingsAccount(acc_no)

            print("Savings Account Created")

        else:

            print("Register Customer First")

    elif choice == "3":

        if current_customer:

            acc_no = input("Account Number: ")

            current_customer.account = CurrentAccount(acc_no)

            print("Current Account Created")

        else:

            print("Register Customer First")

    elif choice == "4":

        if current_customer and current_customer.account:

            amount = float(input("Enter Amount: "))

            current_customer.account.deposit(amount)

            current_customer.transactions.append(
                f"Deposited ₹{amount}"
            )

            print("Deposit Successful")

        else:

            print("Create Account First")

    elif choice == "5":

        if current_customer and current_customer.account:

            amount = float(input("Enter Amount: "))

            if current_customer.account.withdraw(amount):

                current_customer.transactions.append(
                    f"Withdrawn ₹{amount}"
                )

                print("Withdrawal Successful")

            else:

                print("Transaction Failed")

        else:

            print("Create Account First")

    elif choice == "6":

        if current_customer and current_customer.account:

            print("\nCustomer:", current_customer.name)
            print("Balance:", current_customer.account.balance)

        else:

            print("No Account Found")

    elif choice == "7":

        if current_customer:

            print("\n===== TRANSACTION HISTORY =====")

            if len(current_customer.transactions) == 0:

                print("No Transactions Found")

            else:

                for transaction in current_customer.transactions:
                    print(transaction)

        else:

            print("No Customer Selected")

    elif choice == "8":

        if current_customer and current_customer.account:

            interest = current_customer.account.calculate_interest()

            print("Interest =", interest)

        else:

            print("No Account Found")

    elif choice == "9":

        cid = input("Enter Customer ID: ")

        customer = bank.find_customer(cid)

        if customer:

            current_customer = customer

            print("Customer Found")
            print("Name:", customer.name)

        else:

            print("Customer Not Found")

    elif choice == "10":

        if current_customer and current_customer.account:

            print("\n===== ACCOUNT STATEMENT =====")

            print("Customer ID:", current_customer.customer_id)
            print("Customer Name:", current_customer.name)
            print("Balance:", current_customer.account.balance)

            print("\nTransactions:")

            if len(current_customer.transactions) == 0:

                print("No Transactions")

            else:

                for transaction in current_customer.transactions:
                    print(transaction)

        else:

            print("No Account Found")

    elif choice == "11":

        sender_id = input("Sender Customer ID: ")
        receiver_id = input("Receiver Customer ID: ")

        sender = bank.find_customer(sender_id)
        receiver = bank.find_customer(receiver_id)

        if sender and receiver:

            if sender.account and receiver.account:

                amount = float(input("Enter Amount: "))

                if sender.account.withdraw(amount):

                    receiver.account.deposit(amount)

                    sender.transactions.append(
                        f"Transferred ₹{amount} to {receiver.name}"
                    )

                    receiver.transactions.append(
                        f"Received ₹{amount} from {sender.name}"
                    )

                    print("Transfer Successful")

                else:

                    print("Insufficient Balance")

            else:

                print("Both customers must have accounts")

        else:

            print("Customer Not Found")

    elif choice == "12":

        if current_customer and current_customer.account:

            if type(current_customer.account).__name__ == "CurrentAccount":

                current_customer.account.apply_service_charge()

                current_customer.transactions.append(
                    "Monthly Service Charge ₹100"
                )

                print("Service Charge Applied")

            else:

                print("Only for Current Account")

        else:

            print("No Account Found")

    elif choice == "13":

        print("Thank You")
        break

    else:

        print("Invalid Choice")