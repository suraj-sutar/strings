# multiline_string = """
# Sting

# this is multiline string

# """

# print(multiline_string)

# name = 'suraj'

# greeting = "hello, " + name
# print(greeting)

# age = 21

# print("you are age is, " + age)
#you get error in python  you cannot add integer and string together

# if you want to convert this into string
# first you have to convert this integer number to string using

# age = 21

# age_as_str = str(age)

# print("you are age is, " + age_as_str)

# you can use another formate to convert the number into string and print
# you do not use above formate to print number
# you use this f-string to convert number to string
# but using f-string you cannot change the value

# age = 21
# print(f"you are age is: {age}")

# another example
# name = "kashinath"
# greeting = f"how are you, {name}"
# print(greeting)

# name = "yash"
# print(greeting)

# another example
# you caan chenge the string witjout using f-string....

# name = "kashinath"
# final_greeting = "How are you {} ?"
# kashi_greeting = final_greeting.format(name)
# print(kashi_greeting)

# name = "yash"
# final_greeting = "how are you {} ?"
# yash_greeting = final_greeting.format(name)
# print(yash_greeting)

# what this does is it takes the name and it replace the curly braces by the value ie. "kashinath"....
# description = "{} is {age} years old."
# print(description.format("Bob", age=30))