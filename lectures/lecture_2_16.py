#a Tuple is a inmutable data structure
my_tuple = (1,2,3,4)
print(my_tuple)         #prints (1, 2, 3, 4)
print(type(my_tuple))   #prints <class 'tuple'>
print(len(my_tuple))    #prints 4
my_tuple = 2, 5.5, "cat", "rat", 9    # creates a tuple without the '(' and ')'
print(my_tuple)         #prints (2, 5.5, 'cat', 'rat', 9)
print(my_tuple[0])      #prints 2
print(my_tuple[2])      #prints cat
#negative indices start at -1 for the last element, -2 for the second last, etc
print(my_tuple[-2])     #prints the second from the end: rat
#slicing is delimiting a range separated with ':' and excluding the end index
# 1:3 is from the second (included) element up to the fourth one (excluded)
print(my_tuple[1:3])    #prints a tuple with two elements (5.5, 'cat')
