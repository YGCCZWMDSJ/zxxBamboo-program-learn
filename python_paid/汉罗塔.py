n=int(input()) #要移走n个盘子
def hlt(n,s,a,t):
    if n==1:
        print(s+'->'+t)
        return 1
    else:
        hlt(n-1,s,t,a)
        print(s+'->'+t)
        hlt(n-1,a,s,t)

hlt(n,'A','B','C')