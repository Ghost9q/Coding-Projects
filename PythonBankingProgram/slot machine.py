import random
import keyboard
import time
import banking_fanc
# game logic
def play(balance, bet):
    profit = 0
    symbols = ["🍒", "🍋", '7', "💎", "🔔"]
    row = [random.choice(symbols) for _ in range(3)]
    if row == ['🍒', '🍒', '🍒']:
        profit += bet * 2
        account['balance'] += profit
        banking_fanc.save_accounts()
    elif row == ['🍋', '🍋', '🍋']:
        profit += bet * 3
        account['balance'] += profit
        banking_fanc.save_accounts()
    elif row == ['7', '7', '7']:
        profit += bet * 4
        account['balance'] += profit
        banking_fanc.save_accounts()
    elif row == ['💎', '💎', '💎']:
        profit += bet * 5
        account['balance'] += profit
        banking_fanc.save_accounts()
    elif row == ['🔔', '🔔', '🔔']:
        profit += bet * 6
        account['balance'] += profit
        banking_fanc.save_accounts()
    else:
        balance -= bet
        account['balance'] -= bet
        banking_fanc.save_accounts()
    return profit, row
print('--------SL🍊T MACHINE---------')
print("To start playing press 'Enter'")
print("To exit press 'ESC'")
print('''.
   🍒 | 🍒 | 🍒
      
   🍋 | 🍋 | 🍋
      
   7  |  7  |  7 
      
   💎 | 💎 | 💎
      
   🔔 | 🔔 | 🔔''')
print('*****************************')
banking_fanc.load_accounts()
result = ''
# bank account check
while True:
    name = input('Please enter your bank acount username to bet(enter q to quit): ')
    if name == 'q':
         break
    names = [acc['name'] for acc in banking_fanc.accounts]
    if name in names:
        i = banking_fanc.account_index(banking_fanc.accounts, name)
        account = banking_fanc.accounts[i]
        password = input('Enter your password: ')
        if password == account['password']:
             balance = account['balance']
             if balance < 10:
                  print(f'balance: {balance}')
                  print('not enough money in your account')
             else:
                print('Successfully logged in!')
                print(f'balance: {balance}')
                bet = input('Enter the amount you want to bet(10, 50 or 100): ')
                if bet.isdigit() == False:
                    print('Invalid input')
                else:
                    bet = int(bet)
                while bet not in [10, 50, 100]:
                    print('Invalid input!')
                    bet = input('Enter the amount you want to bet(10, 50 or 100 and q to quit): ')
                    if bet.isdigit() == False:
                        print('Invalid input')
                    else:
                        bet = int(bet)
                    if bet == 'q':
                        break
                else:  
                    print("To start playing press 'Space'")
                    print("To exit press 'ESC'")
                    result = 'fine'
                    break
        else:
             print('Wrong password!')
    else:
         print(f'{name} does not exist!')
# main game execution
while result == 'fine':
     if keyboard.is_pressed('space'):
          if account['balance'] < bet: # type: ignore
              print('not enough money in bank account!')
              print('please go to your banking program to deposit to your account!')
              break
          profit, row = play(account['balance'], bet) # type: ignore
          for item in row:
              print(f'{item} | ', end='')
          print()
          if profit == 0:
              print('you lost')
          else:
              print('You won')
          print(f'profit: {profit}')
          print(f'Balance: {account['balance']}') # type: ignore
          print()
          time.sleep(0.2)
     elif keyboard.is_pressed('ESC'):
          print('exiting..')
          break