import sys
import pyperclip

PASSWORDS = {'email': 'qwery1234',
             'blog': '12345password',
             'luggage': '1234567890'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]     # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}')
