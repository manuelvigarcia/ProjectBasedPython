dict={'Japan':'Tokyo','China':'Beijing','Taiwan':'Taipei','South Korea':'Seoul'}

print(dict)

for i in dict:
    print(i)


for k,v in dict.items():
    print(f'The capital of {k} is {v}.')


for i in dict:
    print (i,dict[i])

for i in range(21):
    if (i%2 == 0):
        print(i)
    
