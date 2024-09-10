
#######################
# keyword argument
#######################

def keywordArgument(name, age):
    print(f"{name} is {age} years old")


# must give as separately arguments
print("###########################")
print("Keyword Arguments")
print("###########################")

keywordArgument(name="John", age=56)
keywordArgument(age=24, name="Smith")


#######################
# packed argument
#######################

def sumNum(*var):
    # var is a tuple
    print(type(var))
    total = 0
    for i in var:
        total += i
    print(total)


print("###########################")
print("Packed Arguments")
print("###########################")

# calling the function with packed argument
sumNum(1, 2, 3)


#######################
# named argument
#######################

def namedArgument(**var):
    # var is a dictionary
    print(var["name"])
    print(var["age"])
    print(type(var))


print("###########################")
print("Named Arguments")
print("###########################")

namedArgument(name="John", age=12)

# also can pass like below
sanchitha = {"name": "John", "age": 13}
namedArgument(**sanchitha)
