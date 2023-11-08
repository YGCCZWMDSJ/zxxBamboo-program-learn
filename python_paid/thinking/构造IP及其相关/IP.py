#！python 311
'''
 构造A/B/C类IP地址
- 随机数1，2，3确定构造第几类
- 构造对应构造网络地址
- 考虑子网划分？

查了一下，网上居然有用水仙花数构造的
找网络号和主机号：
'''
########## Begin ##########
def parseIP(ip,mask):
    ipL=ip.split('.')
    maskL=mask.split('.')
    ipL2=['','','','']
    maskL2=['','','','']
    c=0
    for i,j in zip(ipL,maskL):
        ipL2[c]+=bin(int(i))[2:]
        maskL2[c]+=bin(int(j))[2:]
        c+=1
    
    c=0
    for i,j in zip(ipL2,maskL2):
        m,n=len(i),len(j)
        if m!=8:
            ipL2[c]='0'*(8-m)+i
        if n!=8:
            maskL2[c]='0'*(8-n)+j
        c+=1
    netID,hostID=['','','',''],['','','','']
    c=0
    for i,j in zip(ipL2,maskL2):
        for m,n in zip(i,j):
            if m==n=='1':
                netID[c]+='1'
            else:
                netID[c]+='0'
            n_not='0'
            if n=='0':
                n_not='1'
            if m==n_not=='1':
                hostID[c]+='1'
            else:
                hostID[c]+='0'
        c+=1

    net,host=['','','',''],['','','','']
    c1=0
    for i,j in zip(netID,hostID):
        c=7
        r1,r2=0,0
        while c>=0:
            if i[7-c]=='1':
                r1+=2**c
            if j[7-c]=='1':
                r2+=2**c
            c-=1
        net[c1]=str(r1)
        host[c1]=str(r2)
        c1+=1
    net='.'.join(net)
    host='.'.join(host)
    return net,host

########## End ##########
ip = input()   #IP地址
mask = input() #子网掩码
netID, hostID = parseIP(ip, mask)
print('网络号：', netID)   #网络号
print('主机号：', hostID)  #主机号
