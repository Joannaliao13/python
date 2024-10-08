# Python List is like dynamically sized arrays. It is a collection of thing, enclosed in [] and separeted by commas.

# Ex1: Create a list, access element and append one element in this list
mylist = [10,20,30]
print(mylist)                # [10, 20, 30]
print(mylist[0], mylist[1])    # 10 20
mylist.append(40)       
print(mylist)                # [10, 20, 30, 40]


# Ex2: Get the size of list
print(len(mylist))           # 4


# Ex3: Multi-dimensional list
mylist_1=[['Alice','Huang'],['Bill','Lin']]
print(mylist_1[0][0], mylist_1[0][1])  # Alice Huang
print(mylist_1[1][0], mylist_1[1][1])  # Bill Lin

# Ex4: Negative indexing
# negative sequence indexes represent positions from the end of the list.
# -1 refer to the last item, -2 refter to the second-last item, etc.
test=[1,2,3,4,5,6]
print(test[-1])  # 6
print(test[-2])  # 5
print(test[-6])  # IndexError: list index out of range, if index=-7


# Ex5: taking input of a list
string = input("Please input your sentence:")  # How are you today
mystringlist = string.split()
print('-'.join(mystringlist))                  # How-are-you-today

# Ex6: insert() method is for the addition of elements at the desired position.
# insert(position, value)
mylist_2=[1,3,5,7,9]
mylist_2.insert(1,2)  
print(mylist_2)         # [1, 2, 3, 5, 7, 9]
mylist_2.insert(0,'Hi')
print(mylist_2)         # ['Hi', 1, 2, 3, 5, 7, 9]

# Ex7: extend() is used to add multidple elements at the same time at the end of the list.
mylist_2.extend([11, 13, 15])
print(list)         # ['Hi', 1, 2, 3, 5, 7, 9, 11, 13, 15]


# Ex8: reversing a list  
# reversed()
newtuple=(1,2,3,4,5)
print(tuple(reversed(newtuple)))

mylist_3=[1,2,3,4,5]
test_reversed1=list(reversed(mylist_3))
print(test_reversed1)

# reverse() function()
mylist_3.reverse()
print(mylist_3)

# Ex9: Remove elements from the list
# remove(element) function
mylist_3.remove(5)
print(mylist_3)

# pop() function
mylist_3.pop()
print(mylist_3)

# Ex10: Slicing of a List
# user [start_index:end_index]
mylist_4 = ['H','e','l','l','o','W','o','r','l','d']
sliced_list = mylist_4[2:6]
print(sliced_list)       # ['l','l','o','W']
sliced_list = mylist_4[3:]
print(sliced_list)       # ['l','o','W','o','r','l','d']
sliced_list = mylist_4[:5]
print(sliced_list)       # ['H','e','l','l','o']

# negative index
sliced_list = mylist_4[-6:-1]
print(sliced_list)       # ['o', 'W', 'o', 'r', 'l']

# we could use slice operation to reverse the list
sliced_list = mylist_4[::-1]
print(sliced_list)       # ['d', 'l', 'r', 'o', 'W', 'o', 'l', 'l', 'e', 'H']


# Ex11: List Comprehension
# used for creating new list from other iterables.
square_odd = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(square_odd)        # [1, 9, 25, 49, 81]

# Ex12: clear():Remove all the items
square_odd.clear()
print(square_odd)        #[]

# Ex13: count(): used to count the occurrance of the element
my_list5 = [1,3,2,4,5,5,5,1,1,2,1]
print(my_list5.count(1))  #4













