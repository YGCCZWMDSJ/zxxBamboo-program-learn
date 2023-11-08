def deelList(spam):
    for i in range(len(spam)-2):
        if len(spam)-2<0:
            break
        print(spam[i],end=',')
    if len(spam)-2==-1:
        print(spam[0])
    else:
        print(spam[-2]+' and '+spam[-1])

spam=['aooles']
deelList(spam)