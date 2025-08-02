import json
import os
from datetime import datetime
# Path to save your accounts data
DATA_FILE = 'accounts.json'

def save_accounts():
    with open(DATA_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def load_accounts():
    global accounts
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            accounts = json.load(f)
    else:
        accounts = []

def add_acount(name,password):
    accounts.append({'name':name,
                    'password':password,
                    'balance': 0,
                    'history': []})

def account_index(accounts1, name):
    for i, acc in enumerate(accounts1):
        if acc["name"] == name:
            return i
    return -1  # Not found

def remove_acount(name, password):
    i = account_index(accounts, name)
    account = accounts[i]
    if password == account['password']:    
        accounts.pop(i)
    else:
        return -1
            
def deposit(account, amount):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if amount <= 10000:
        account['balance'] += amount
        account['history'].append({
                "type": "deposite",
                "amount": amount,
                "time": current_time
            })
    else:
        return -1
        

def withrawl(account,amount):
    if amount <= account['balance']:
        account['balance'] -= amount
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account['history'].append({
                "type": "withrawl",
                "amount": amount,
                "time": current_time
            })
    else:
        return -1


def main():
    print('THIS IS AN EXAMPLE ON HOW TO USE THE CODE!')
    print("""add_acount('shokran', '878342')
    print(accounts)
    deposite('shokran', 400)
    print(accounts)
    withrawl('shokran', 300)
    print(accounts)
    print(display_balance('shokran'))""")
    
if __name__ == '__main__':
    main()