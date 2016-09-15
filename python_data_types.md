# types of data
#  - integer
#  - float
#  - bool
#  - chars
#  - strings
#  - etc

# booleans - Either True or False
t = True
type(t)  # class 'bool'


# >>> bool(42)
# True
# >>> bool('happy go lucky')
# True
# >>> bool(0)
# False
# >>> bool('')
# False
# >>>

# == equal to
# != not equal to
# > greater
# < less
# >= greater than or equal
# <= less than or equal

# >>> answer = 10 >= 12
# >>> answer
# False

# and, or not to combine multiple operations


# >>> li = []
# >>> other_li = [1, 2, 3]
# >>> li.append(1)
# >>> li.append(5)
# >>> li.append(3)
# >>> li
# [1, 5, 3]
# >>> li.pop()
# 3
# >>> li
# [1, 5]
# >>> li[0]
# 1

# tuples are immutable lists, most of the same operations that can be done on lists can be done here.

# >>> bookmark1 = (35,5)
# >>> bookmark2 = (86, 15)
# >>> bookmark3 = (106, 11)
# >>> notes = [bookmark1, bookmark2, bookmark3]
# >>> notes
# [(35, 5), (86, 15), (106, 11)]



# >>> my_set = {1,2,2,3,4,5,6,7}
# >>> my_set
# {1, 2, 3, 4, 5, 6, 7}
# >>> your_set = {6,7,8,9,10}
# >>> your_set
# {8, 9, 10, 6, 7}
# >>> my_set & your_set
# {6, 7}
# >>> my_set | your_set
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# >>> my_set - your_set
# {1, 2, 3, 4, 5}
# >>> 1 in my_set
# True

#  Lists have order, tuples have structure, and sets are mathematical

# stooges = {'Larry': 'balding with frazzled hair',
#            'Curly': 'short buzz cut',
#            'Moe':  'bowl cut'}
# 
# stooges['Larry'] # 'balding with frazzled hair'
# 
# stooges.keys() # returns the keys, ie names in this example
# stooges.values() # returns their attribute in this example