# string and numeric value can operate together with "*"
a,b=2,3
txt="@"
print(2*txt*8)

# string and sring can operate with "+"
a,b="2",3
txt="@"
print((a+txt)*b)

#arithmatic expression with integer and float will result in float

a,b=10,5.0
c=a*b
print(c)

# Numeric values can operate with all arithmatic operators
a,b=2,3
c=4
print(a+b*c)

# Result of division operator with two integers will be float
a,b=2,3
c=a/b
print(c)

# Integer division with float and int will give int displayed as float

a,b=1.5,3
c=a//b
print(c,a/b)