import random
import math
n=5000
sum=0.0
list=[]
for k in range(100):
    m=0
    pie=math.pi
    for i in range(n):
        x=1
        for j in range(8):
            r=random.uniform(0.0,pie)
            x+=math.cos(r)
            if (x<=0):
                m=m
                break
            elif (x>=4): # 5 is shielding width
                m+=1
                break
    per=(100*float(m))/float(i)
    list.append(per)
    sum+=per
print "average percent that make it: ",float(sum)/float(100)
