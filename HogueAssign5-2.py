from decimal import Decimal
import math

def heron(a,b,c):
	s=(a+b+c)/2
	A=math.sqrt(s*(s-a)*(s-b)*(s-c))
	return A
d=heron(3.0,3.0,3.0)
print d
