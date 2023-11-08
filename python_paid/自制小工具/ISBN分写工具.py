import re
num=input()
if re.match(r'^978',num):
    print(num[0:3]+'-'+num[3]+'-'+num[4:7]+'-'+num[7:12]+'-'+num[12])
else:
    print(num[0]+'-'+num[1:4]+'-'+num[4:9]+'-'+num[9])