#! python3
# pw.py - An insecure password locker program.

PASSWORDS={'email':'F7mineh3euidbhewdjhjn',
           'blog':'sjdxhjedhwkjddxcjhcuhu78uhgx',
           'luggage':'21142345'}

import sys,pyperclip
if len(sys.argv)<2:
    print('Usge:python pw.py[account] - copy account password')
    sys.exit()

account=sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named '+account)