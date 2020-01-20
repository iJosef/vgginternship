account_details = {}

def user_verification(email):
    if email in account_details.keys():
        return email
    return False

def check_password(password,confirm_password):
    if len(password) > 5:
        if password == confirm_password:
            return password
    else:
        return False

def create_account():
    print("\nCREATE NEW ACCOUNT\n")
    new_email = str(input("Enter a valid email: ")).lower()

    #check email format~
    if len(new_email) > 5 and ('@' in new_email) and ('.' in new_email):
        
        if user_verification(new_email):
            print("Email Already exists! Try again")
            create_account()
        else:
            new_password = str(input("Enter a valid password: "))
            confirm_password = str(input("Confirm password: "))

            if check_password(new_password, confirm_password):
                account_details[new_email] = {'password' : new_password, 'balance': 0.00}
                print("Account created successfully!")
                landing_page()
            else:
                print("****** Invalid Password ******\n")
                create_account()
    else:
        print("Invalid Email address")
        create_account()


def authenticate_user():
    print("\n>>>>>>>>> LOG IN <<<<<<<<\n")
    user_email = str(input("Enter email: ")).lower()
    user_password = str(input("Enter password: "))

    if user_email in account_details.keys():
        if account_details[user_email]['password'] == user_password:
            transaction_options(user_email)
    else:
        print("User don't exist! Create Account\n" )
        create_account()


def transaction_options(account):
    print("\n******* TRANSACTION PAGE *********\n")
    more_options = int(input(''' Press 1: check balance
     Press 2: deposit
     Press 3: withdraw
     Press 4: transfer
     Press 0: To return to home
     '''))
    if more_options == 1:
        check_balance(account)
    elif more_options == 2:
        make_deposit(account)
    elif more_options == 3:
        make_withdrawal(account)
    elif more_options == 4:
        make_transfer(account)
    elif more_options == 0:
        landing_page()
    else:
        print("Enter a valid action")
    transaction_options(account)


def check_balance(account):
    print("\n====================== CHECK BALANCE ===================\n")
    print("Your account balance is: ", account_details[account]['balance'])
    transaction_options(account)


def make_deposit(account):
    print("\n====================== MAKE DEPOSIT ===================\n")
    deposit_amount = int(input("Input amount to be deposited:\n"))
    account_details[account]['balance'] = account_details[account]['balance'] + deposit_amount
    new_balance = account_details[account]['balance']

    print("Amount deposited: ", deposit_amount, "\nAvailable balance: ", new_balance)
    transaction_options(account)


def make_withdrawal(account):
    print("\n====================== MAKE WITHDRAWAL ===================\n")
    amount = int(input("Input amount to withdraw:\n "))
    
    if bank_accounts[account]['balance'] == 0.00:
        print("You have no money in your account. Kindly make deposit and try again.\n")
        make_deposit(account)
    elif bank_accounts[account]['balance'] < amount:
        print("Cannot withdraw more than you have in your account\n ")
        make_deposit(account)
    else:
        account_details[account]['balance'] = account_details[account]['balance'] - amount
        current_balance = account_details[account]['balance']
        print("\n============== Withdrawal Successful ==========\n Amount withdrawn: ", amount, "\nCurrent available balance: ", current_balance)
    transaction_options(account)


def make_transfer(account):
    print("\n====================== MAKE TRANSFER ===================\n")
    transfer_amount = int(input("Enter amount to be transfered: "))
    beneficiary = str(input("Enter beneficiary's email: ")).lower()

    if transfer_amount > account_details[account]['balance']:
        print("You have *** insuffient *** funds to perform transaction! Kindly make deposit and try again\n")
        transaction_options(account)
    else:
        if verify_account(beneficiary):
            account_details[beneficiary]['balance'] = account_details[beneficiary]['balance'] + transfer_amount

            # User's current balance after making a transfer
            account_details[account]['balance'] = account_details[account]['balance'] - transfer_amount
            account_balance = account_details[account]['balance']
            print("------- Transfer Successful -------\nAmount transfered: ", transfer_amount, "\nBeneficiary's email: ", beneficiary, "\nAccount Balance: ", account_balance)
            transaction_options(account)
        else:
            print("\n------- Invalid Beneficiary -----\n Kindly verify email address")
            transaction_options(account)


def landing_page():
    print("\n>>>>>>>>>>>>> HOME PAGE <<<<<<<<<<<<<<<<<")
    welcome_page = int(input("Hello,\n Press 1: create account\n Press 2: transaction\n Press 0: Quit program\n"))
    
    if welcome_page == 1:
        create_account()

    elif welcome_page == 2:
        authenticate_user()

    elif welcome_page == 0:
        quit()
    else:
        print("Enter a valid option")
        landing_page()

landing_page()







