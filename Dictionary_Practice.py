# A dictionary is a data structure that stores the value in key: value pairs.

# Ex1: Sereval ways to create a dictionary
# 1:
mydict_1 = {1: 'How', 2: 'Are', 3: 'You'}
print(mydict_1)      # {1: 'How', 2: 'Are', 3: 'You'}

#2
mydict_1 = dict({1: 'I', 2: 'Am', 3: 'Great'})
print(mydict_1)      # {1: 'I', 2: 'Am', 3: 'Great'}

#3
mydict_1 = dict([(1, 'Good'), (2, 'Bye')])
print(mydict_1)      # {1: 'Good', 2: 'Bye'}

# Ex2: add element
mydict_1[0] = 'Go'
mydict_1[4] = 'Home'
print(mydict_1)      # {1: 'Good', 2: 'Bye', 0: 'Go', 4: 'Home'}

# Ex3: get data
print(mydict_1.get(0))  # Go

# Ex4: delete an element
#use del() function
del(mydict_1[2])
print(mydict_1)                # {1: 'Good', 0: 'Go', 4: 'Home'}

# Ex5: return the keys
# use keys()
print(mydict_1.keys())         # dict_keys([1, 0, 4])

# return items, use items()
print(mydict_1.items())        # dict_items([(1, 'Good'), (0, 'Go'), (4, 'Home')])

# return values, use values()
print(mydict_1.values())       # dict_values(['Good', 'Go', 'Home'])

# Ex6: return True/False to see the key in the list or not.
#(1)
mydict_2 = {'A': 65, 'B': 66, 'C': 68}
print(mydict_2.__contains__('A'))      # True

#(2)
if 'B' in mydict_2:
    print(mydict_2['B'])     # 66

# Ex7: update the value
mydict_2.update({'C': 67})
print(mydict_2)





