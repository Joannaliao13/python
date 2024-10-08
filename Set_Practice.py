# Set is a unordered collection data, it has no duplicate elements.
# It is represented by {....}

# Ex1:
myset = set(["X", "Y", "Z"])
print(myset)         # {'Y', 'Z', 'X'}

# Adding element to the set
myset.add("W")
print(myset)         # {'Y', 'W', 'Z', 'X'}

# Ex2:
# can store heterogeneous elements
myset = {"No", 1, 2, "Problem", 3.14, True}
print(myset)         # {1, 2, 3.14, 'Problem', 'No'}


# Ex3: add elements
myset_1={'Lin', 'Chen', 'Wu'}
myset_1.add('Liao')
print(myset_1)       # {'Lin', 'Wu', 'Liao', 'Chen'}

# Ex4: merge two sets
myset_2 = {'Huang', 'Chiang'}
myset_3 = myset_1.union(myset_2)
myset_4 = {'Red', 'Black'}
print(myset_3)       # {'Lin', 'Wu', 'Liao', 'Chiang', 'Chen', 'Huang'}

# use | (or) to union two sets
myset_5 = myset_2 | myset_4
print(myset_5)       # {'Huang', 'Red', 'Black', 'Chiang'}


# Ex5: intersection of sets
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)
print(set1)        # {0, 1, 2, 3, 4}

for i in range(2,8):
    set2.add(i)
print(set2)        # {2, 3, 4, 5, 6, 7}

# intersection() function
set3 = set1.intersection(set2)
print(set3)          # {2, 3, 4}

# Ex6: find differneces of sets
# use difference() 
set3 = set1.difference(set2)
print(set3)          # {0, 1}

set3 = set1-set2
print(set3)           # {0, 1}


# Ex7: Symmetric Difference
set3 = set1 ^ set2    # {0, 1, 5, 6, 7}
print(set3)

print(6 in set3)      # True


# Ex8: clear set
set3.clear()
print(set3)



