import random
offspring=1
p1=4.0/11.0
p2=1.0/11.0
n=21
nn=100.0
sum=0.0
tally=0.0
for l in range(nn):
	for i in range(1,n):
		print i
		if offspring>0:
			off=offspring
			offspring=0
			for j in range(off):
       	 			p=random.uniform(0,1)
				if p<p1:
					offspring+=1
				if p<p2:
					offspring+=2
		else:
			if i==20:
				tally+=1
			sum+=i
			break
average=float(sum)/float(nn)
print "the sum of all offspring within 100 trials: ",sum
print "the average number of offspring within 100 trials: ",average
print "the probability that the royal family male line will die off after 20 generations is: ", float(tally)/nn
