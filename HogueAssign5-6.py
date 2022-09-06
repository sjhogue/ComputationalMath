n=int(raw_input("enter a natural number: "))
for k in range (2,10000000,1):
	if (n==1):
		print 1
		break
	if (n%k==0):
		print k
		break
