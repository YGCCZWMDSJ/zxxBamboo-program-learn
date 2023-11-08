def collatz(number):
    if number % 2 ==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

def inputNum():
    try:
        print('Please input a number:',end='')
        num=abs(int(float(input())))
        while num not in(0,1):
            num=collatz(num)
            if num == 1:
                pass
    
    except ValueError:
        print('please input a int')
        inputNum()

inputNum()
print('None')