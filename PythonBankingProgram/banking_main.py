import banking_fanc
print('''
-----------WELCOME TO YOUR BANK-----------''')
print('''To add acount: 'a'
to remove acount: 'r'
to deposit: 'd'
to withdraw: 'w'
to see account and balance/history: 's'
to quit: 'q'
''')
banking_fanc.load_accounts()
# main process
while True:
    choice = input('Enter (a/r/d//w/q): ').lower()
    if choice in ['a', 'r', 'd', 'w', 'q','s']:
        if choice == 'q':
            print('bye')
            break
        elif choice == 'a':
            names = [acc['name'] for acc in banking_fanc.accounts]
            name = input('Enter a name for your new account: ').strip()
            while name in names:
                print(f'{name} already exists')
                name = input('Enter a name for your new account(q to quit): ').strip()
                if name == 'q':
                    break
            else:
                password = input('enter a password for your account: ').strip()
                banking_fanc.add_acount(name, password)
                banking_fanc.save_accounts()
# Remove account
        elif choice == 'r':
            name_r = input('Enter an acount username to remove: ').strip()
            names = [acc['name'] for acc in banking_fanc.accounts]
            if name_r in names:
                password = input('enter your password: ').strip()
                which = banking_fanc.remove_acount(name_r, password)
                while which == -1:
                    print('wrong password!')
                    password = input('enter your password(q to quit): ').strip()
                    which = banking_fanc.remove_acount(name_r, password)
                    if password == 'q':
                        break
                else:
                    print(f'{name_r} Removed!')
                    banking_fanc.save_accounts()
            else:
                print(f'{name_r} does not exist')
# deposit
        elif choice == 'd':
            name = input('Enter your user name: ').strip()
            names = [acc['name'] for acc in banking_fanc.accounts]
            if name in names:
                password = input('Enter your password: ').strip()
                i = banking_fanc.account_index(banking_fanc.accounts, name)
                account = banking_fanc.accounts[i]
                while password != account['password']:
                    print('Wrong password!')
                    password = input('Enter your password(q to quit): ').strip()
                    if password == 'q':
                        break
                else:
                    amount = int(input('Enter the amount you want to deposit: '))
                    which = banking_fanc.deposit(account, amount)
                    while which == -1:
                        print('amount cannot be more than $10000')
                        amount = input('Enter the amount you want to deposit(q to quit): ')
                        if amount == 'q':
                            break
                        which = banking_fanc.deposit(account, int(amount))
                    else:
                        print(f'Succesfully depositd ${amount}.')
                        banking_fanc.save_accounts()
            else:
                print(f'{name} does not exist')
# Withdraw
        elif choice == 'w':
            name = input('Enter your user name: ').strip()
            names = [acc['name'] for acc in banking_fanc.accounts]
            if name in names:
                password = input('Enter your password: ').strip()
                i = banking_fanc.account_index(banking_fanc.accounts, name)
                account = banking_fanc.accounts[i]
                while password != account['password']:
                    print('Wrong password!')
                    password = input('Enter your password(q to quit): ').strip()
                    if password == 'q':
                        break
                else:
                    amount = int(input('Enter the amount you want to withrawl: '))
                    which = banking_fanc.withrawl(account, amount)
                    if which != -1:
                        banking_fanc.save_accounts()
                    while which == -1:
                        print('Incifecuint Balance')
                        amount = input('Enter the amount you want to withrawl(q ot quit): ')
                        if amount == 'q':
                            break
                        which = banking_fanc.withrawl(account, int(amount))
                    else:
                        print(f'Succesfully withrawled ${amount}.')
            else:
                print(f'{name} does not exist')
                banking_fanc.save_accounts()
# Show balance
        elif choice =='s':
             name = input('Enter your user name: ').strip()
             names = [acc['name'] for acc in banking_fanc.accounts]
             if name in names:
                password = input('Enter your password: ').strip()
                i = banking_fanc.account_index(banking_fanc.accounts, name)
                account = banking_fanc.accounts[i]
                while password != account['password']:
                    print('Wrong password!')
                    password = input('Enter your password(q to quit): ').strip()
                    if password == 'q':
                        break
                else:
                    print('-------BALANCE-------')
                    print(f"${account['balance']}")
                    print('-------HISTORY-------')
                    for history in account['history']:
                        print(f"{history['time']}: {history['type']}   ${history['amount']}")
             else:
                 print(f'{name} does not exist.')
    else:
        print('Invalid input!')