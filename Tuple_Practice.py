# Tuple is a collection of programming objects much like a list.
# The sequence of values stored in a tuple can be of an type, and they are indexed by integers.
# The data in the tuple cannot be modified/ deleted.


# Ex1:
tuple1 = (1, 'Welcome', 3, 'Customer')
print(tuple1)              # (1, 'Welcome', 3, 'Customer')
print(tuple1[1])           # Welcome
print(tuple1[1][0])        # W
tuple2 = (4, 5, 2, 3)
print(tuple1, tuple2)      # (1, 'Welcome', 3, 'Customer') (4, 5, 2, 3) 

# Ex2: Unpacking
a, b, c, d = tuple2
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)
print(d)

# Ex3: Concatenation
tuple3 = tuple1 + tuple2
print(tuple3)            # (1, 'Welcome', 3, 'Customer', 4, 5, 2, 3)


# Ex4: Sliced 
tuple1 = tuple('HelloGoodMorning')
print(tuple1[5:])         # ('G', 'o', 'o', 'd', 'M', 'o', 'r', 'n', 'i', 'n', 'g')
print(tuple1[:7])         # ('H', 'e', 'l', 'l', 'o', 'G', 'o')
print(tuple1[::-1])       # ('g', 'n', 'i', 'n', 'r', 'o', 'M', 'd', 'o', 'o', 'G', 'o', 'l', 'l', 'e', 'H') 

# Ex5: delete a tuple
del tuple1
print(tuple1)           # NameError: name 'tuple1' is not defined. tuple1 has been deleted.












