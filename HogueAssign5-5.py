import math
from decimal import Decimal
def myquadsolve(a,b,c):
	disc=b**2-4*a*c
	if (disc>0): 
		dis =Decimal(str(math.sqrt(b**2 - 4*a*c)))
		r1 = (-b + dis) / (2*a)
		r2 = (-b - dis) / (2*a)
		print "The real roots for this quadratic are ",r1 ,"and", r2
	elif (disc==0):
		dis=Decimal(str(math.sqrt(b**2-4*a*c)))
		r1=(-b+dis)/(2*a)
		print "The only real root for this quadratic is ",r1
	else:
		print "There are no real roots to this quadratic"
d=Decimal(raw_input("enter the value for a: "))
e=Decimal(raw_input("enter the value for b: "))
f=Decimal(raw_input("enter the value for c: "))

myquadsolve(d,e,f)
