import matplotlib.pyplot as plt
X = [0,  0.5,   1,   1.5,   2,  2.5,   3,   4,  4.5,    5]
Y = [0,   18,  20,  39.5,  60,   50,  68,  77,  100,  110]
########## Begin ##########
hxk,hyk,hxkdotyk,hxkf=0,0,0,0
for x in X:
    hxk+=x
    hxkf+=x**2
for y in Y:
    hyk+=y
for x,y in zip(X,Y):
    hxkdotyk+=x*y
n=len(X)
k=(hxk*hyk-n*hxkdotyk)/(hxk**2-n*hxkf)
b=(hxk*hxkdotyk-hxkf*hyk)/(hxk**2-n*hxkf)
plt.plot(X,Y,'bo')
y=0
Y1=[]
for x in X:
    y=k*x+b
    Y1.append(y)
plt.plot(X,Y1,'r-')
########## End ##########
print('y = %.3fx + %.3f' % (k,b))
plt.savefig( 'pic.png' )
plt.close()