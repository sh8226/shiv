#name:shiv prakash
#roll no:16IM10020
import numpy as np
import math
import matplotlib.pyplot as plt
from random import*
p=.20
q=np.zeros(100)
#initilizing a list 
y=[]
#value of percentage error
L=.05*p
#value of sigma
sigma=.005
l=math.pow(L,2)
#define a function which take p,sigma as an argument.
def function(p,l,sigma,q):
    r=np.zeros(100)
    for i in range(0,100):
        y.append(np.random.normal(p,3*sigma))#add random value in each iteration
        ub=p+3*sigma# upper limit 
        lb=p-3*sigma #lower limit
        if y[i]>ub or y[i]<lb:
            q[i]=np.random.randint(0,2)
            if q[i]==1:
                p=0
                for j in range(0,i+1):
                    p=p+y[j]
                p=p/(i+1)
                n=3.84*p*(1-p)/l
                sigma=math.sqrt(l/3.84)
                review(y,sigma,j,p,r)
            else:
                y[i]=p
    return(y,ub,lb,p);
#function for revising the value of p
def review (y,sigma,i,p,r):
    ub=p+3*sigma
    lb=p-3*sigma
    for j in (0,i):
        if y[j]>=ub or y[j]<=lb:
            q[j]=np.random.randint(0,2)
            if r[j]==1:
                p=0
                for k in range(0,j+1):
                    p=p+y[k]
                    p=p/(j+1)
                    n=3.84*p*(1-p)/l
                    sigma=math.sqrt(l/3.84)
                    review(y,sigma,j,p,r)
            else:
                y[j]=p
    return (y,ub,lb,p);
s=[]
x=list(range(100))
y,ub,lb,p=function(p,l,sigma,q)
print('the final mean:',p)
for i in range(0,100):
    s.append(y[i])
plt.plot(x,s,'bo')
plt.plot([0,100],[lb,lb],label="lower bound")
plt.plot([0,100],[ub,ub],label="upper bound")
plt.plot([0,100],[p,p],label='mean')
plt.ylabel('p value')
plt.xlabel('days')
plt.legend()
plt.show()
    
