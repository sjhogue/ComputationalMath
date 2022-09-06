import random
import math

step=1
ps=1.0/6.0
pn=ps+1.0/4.0
pe=pn+1.0/4.0
pw=pe+1.0/3.0
sum=0.0
n=100
tally=0.0
for k in range(n):
	x=0
	y=0
	for i in range(50):
		p=random.uniform(0,1)
		if p<ps:
			y-=step
		elif p<pn:
			y+=step
		elif p<pe:
			x+=step
		else:
			x-=step
	distance=math.sqrt((0-x)**2+(0-y)**2)
	other_distance=abs(x)+abs(y)
	if distance>20:
		tally+=1
	sum+=distance
average=sum/n
print "probability of being more than 20 units from the origin: ",tally/n
print "average unit distance from the origin:",  average, "units"
