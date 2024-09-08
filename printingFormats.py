name = "xyz"
disease = "covid19"

print("The name os virus is ", name)

# using .format() method
print("The name of virus is {}".format(name))
print("{} is the name of virus.".format(name))

# multiple variables using .format() method
print("The name of virus is {} and it causes {}".format(name, disease))

print(f"The name of virus is {name} and it causes {disease}")

# Concatenation
print("The name of virus is" + " " + name)
