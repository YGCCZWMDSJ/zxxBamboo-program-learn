catName=[]
while True:
    print('cat'+str(len(catName)+1)+':',end='')
    name=input()
    if name=='':
        break
    catName=catName+[name]

print('the cat names are:',end='')
for name in catName:
    print(name,end=' ')

print()
choose=input()
if choose not in catName:
    print('it is not in here,please choose other.')
else:
    print('You choose '+choose+' success.')