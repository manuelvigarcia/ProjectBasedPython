#accept input from user
var = input("What is your name? ")
print(f"Hello {var}!!")
print(type(var))

var2 = input("How old are you? ")
print(var2)
print(type(var2))

age = int(input("How old are you? "))
print(type(age))
of_age = ""
if (age < 18): of_age = "not "
print("you are "+ of_age +"an adult.")
print(type(age))