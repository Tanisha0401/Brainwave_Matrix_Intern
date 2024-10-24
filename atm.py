def atm_interface():
    print("Please Insert Your Card")
    print("-------------------------------------------")
    pin = input("Enter Your ATM Pin: ")
    
    if pin == "1234":  
        atm = ATM()  
        while True:
            print("\n        1 == Balance")
            print("        2 == Withdraw Money")
            print("        3 == Deposit Money")
            print("        4 == Exit")
            print("------------------------------------------")
            try:
                print("----------------------------------------")
                choice = int(input("\nPlease enter your choice: "))
                print("------------------------------------------------")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")
                continue
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                try:
                    amount = float(input("Enter the amount to withdraw:"))
                    atm.withdraw(amount)
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
                    print("-----------------------------------------------------")
            elif choice == 3:
                try:
                    amount = float(input("Enter the amount to deposit:"))
                    atm.deposit(amount)
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
                    print("---------------------------------------------")
            elif choice == 4:
                atm.exit_atm()
                break
            else:
                print("Invalid choice! Please select a valid option.")
                print("--------------------------------------------")
    else:
        print("Invalid PIN! Please try again.")
        print("-----------------------------------------------")
if __name__== "__main__":
    atm_interface()