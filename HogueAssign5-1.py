from decimal import Decimal
principal=int(raw_input("Enter the principal amount: "))
rate=Decimal(raw_input("Enter the annual rate: "))
A=principal*(1+rate)**1
B=principal*(1+rate)**4
C=principal*(1+rate)**12
D=principal*(1+rate)**365
print "Amount after one year of annual compounding: $",A
print "Amount after one year of quarterly compounding: $",B
print "Amount after one year of monthly compounding: $",C
print "Amount after one year of daily compounding: $",D

