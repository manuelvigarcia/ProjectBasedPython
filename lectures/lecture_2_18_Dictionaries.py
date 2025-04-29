#Dictionaries are collections of key-value pairs.
dict={'Japan':'Tokio','China':'Beijing','South Korea':'Seoul','North Korea':'Pyongyang','a':3}
print(dict)              #prints {'Japan': 'Tokio', 'China': 'Beijing', 'South Korea': 'Seoul', 'North Korea': 'Pyongyang', 'a': 3}
print(len(dict))         #prints 5
print(dict.keys())       #prints dict_keys(['Japan', 'China', 'South Korea', 'North Korea', 'a'])
print(dict.values())     #prints dict_values(['Tokio', 'Beijing', 'Seoul', 'Pyongyang', 3])
#copy into a second dictionary and alter the copy
dict2 = dict.copy()
del(dict2['a'])
print(dict2)      #prints {'Japan': 'Tokio', 'China': 'Beijing', 'South Korea': 'Seoul', 'North Korea': 'Pyongyang'}
#original dictionary not affected
print(dict)       #prints {'Japan': 'Tokio', 'China': 'Beijing', 'South Korea': 'Seoul', 'North Korea': 'Pyongyang', 'a': 3}
#Adding new pair: <variable_name>["<new_key>"]=<new_value>
dict2["HK Sar"]='Hong Kong'
dict2[10]="bullseye"
print(dict2)      #prints {'Japan': 'Tokio', 'China': 'Beijing', 'South Korea': 'Seoul', 'North Korea': 'Pyongyang', 'HK Sar': 'Hong Kong', 10: 'bullseye'}
#get the value for a given key
print(dict2[10])       #prints bullseye
print(dict2['China'])  #prints Beijing
print('a' in dict)     #prints True
print('a' in dict2)    #prints False
print('b' in dict2)    #prints False
print('a' not in dict2)    #prints True


