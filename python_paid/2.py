import sys

while True:
    print('The exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed'+response+'.')