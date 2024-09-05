def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
def deposit():
    amount = float(input("Enter n amount to be deposited: "))

    if amount < 0:
        print("This is not avalid amount!!")

    else:
        return amount
def withraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
def main():
        
    balance = 0
    is_running = True

    while  is_running:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("  Banking programe  ")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
        
        print("1.Show Balnce")
        print("2.Deposit")
        print("3.withdraw")
        print("4. Exist")

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^")


        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("That is not avalid choice")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^")

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^")    
    print("Thank you have anyc day")
    

if__name__ = '__main__'
main()