def pyramid(n):
	sum=0
	for i in range(1,n+1,1):
		square=i**2
		sum=sum+square
		print sum
pyramid(3)
