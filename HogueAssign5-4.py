def sort3(a,b,c):
	biggest=a
	if (biggest<b):
		biggest=b
	if (biggest<c):
		biggest=c
	smallest=a
	if (smallest>b):
		smallest=b
	if (smallest>c):
		smallest=c
	middle=a
	if ((middle<b and middle<c) or (middle>b and middle>c)):
		middle=b
	if ((middle<a and middle<c) or (middle>a and middle>c)):
		middle=c
	return smallest, middle, biggest
sorted=sort3(6,7,1)
print sorted
