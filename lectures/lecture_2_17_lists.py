#a list is a mutable list of heterogeneous elements and it is represented in '[' ']'
my_list = list("programiz")
print(my_list) #prints ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
mfood = ['eggs', 'coffee', 'apple', 'cheese cube'] #prints ['eggs', 'coffee', 'apple', 'cheese cube']
print(mfood)
nos = [4,56,7,11,15]
print(nos)            #prints [4, 56, 7, 11, 15]
mix = [4,1,7,25,'cat','dog','rat']
print(mix)            #prints [4, 1, 7, 25, 'cat', 'dog', 'rat']
#One element can be another list
mix2=[12,2,'egg',32,'coffee', nos]
print(mix2)           #prints [12, 2, 'egg', 32, 'coffee', [4, 56, 7, 11, 15]]
#build from scratch
contact = []
contact.append('Gary')
print(contact) #prints ['Gary']
contact.append('Mary')
print(contact) #prints ['Gary', 'Mary']
contact.extend(['Ray','Tia',3,8,2])
print(contact) #prints ['Gary', 'Mary', 'Ray', 'Tia', 3, 8, 2]
#insert at index
contact.insert(2,'Molly')
print(contact) #prints ['Gary', 'Mary', 'Molly', 'Ray', 'Tia', 3, 8, 2]
nos2=[2,7,14,5,26,19,30,35]
print(nos2)      #prints [2, 7, 14, 5, 26, 19, 30, 35]
nos2.remove(14)
print(nos2)      #prints [2, 7, 5, 26, 19, 30, 35]
del nos2[3]
print(nos2)      #prints [2, 7, 5, 19, 30, 35]
rno = nos2.pop(2)
print(rno)         #prints 5
print(nos2)        #prints [2, 7, 19, 30, 35]
print (nos2[0])    #prints 2
print (nos[1:4])   #prints [56, 7, 11]
#replacing elements in the list
nos2[1]=5
print(nos2)        #prints [2, 5, 19, 30, 35]
