# Examples in converting String to Numbers and Numbers to strings.

# Ex1: Convert a String to Int
mystr = "10"
print(f'String to Int: {int(mystr)+20}')  # string to int:30


# Ex2: Convert a String to Float
mystr = "10"
print(f'String to Float:{float(mystr)+2.0}')  # string to float:12.0


# Ex3: Covert Int to String
myint = 200
print(f'Int to String:{str(myint)+"100"}')   # int to string:200100

# Ex4: Convert Float to String
myfloat = 10.123
print(f'Float to String:{str(myfloat)+"456"}')  # Float to String:10.123456


# Ex5: Covert Float to String 
#      using format() function 
myfloat = 22.345
print("New String is {}".format(myfloat))  # New String is 22.345


# Ex6: Covert String to Int 
#      using eval() function
mystr="999"
print(f'eval("999")+1: {eval(mystr)+1}')  # eval("999")+1:1000


# Ex7: Covert String to Float 
#      using eval() function
mystr="1000.001"
print(f'eval("1000.001")+111: {eval(mystr)+111}')  # eval("1000.001")+111:1111.001


# Ex8: Decimal number
# Arithmetric operations on the floating number can give some unexpected answer.
# We can use decimal() to aviod this situation.
a = 1.1
b = 2.2
c = a + b
d = b - a
print(c)    # 3.300000000000003 (unexpected answer)
print(d)    # 1.100000000000001 (unexpected answer)

# use Decimal() to solve the problem
import decimal
A = decimal.Decimal('1.1')
B = decimal.Decimal('2.2')
C = A + B
print(C)    # 3 (expected answer)


