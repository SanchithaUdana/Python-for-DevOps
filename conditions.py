# IF Condition

x = 21

if x < 30:
    print("Inside IF block")
    print("X is less than 30")

print("Rest of the code.")

x = 31

if x < 30:
    print("Inside IF block")
    print("X is less than 30")

print("Rest of the code.")


# If/Else Condition
x = 31

if x < 30:
    print("Inside of block")
    print("X is less than 30")
else:
    print("Inside else block")
    print("x is greater than 30")

# If/Elif/Else Condition
x = 40

if x > 40:
    print("X is greater than 40")
elif x == 40:
    print("X is equal to 40")
else:
    print("X is less than 40")



"""
This script will implement our knowledge on
conditions and different datatypes.
"""
print("This IT Organization has various skill sets.")
print("Find out your match.")

print("Enter Capitalised Values: ")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code":1218}

usr_skill = input("Enter your desired skill: ")

# Check in the database if we have this skill
if usr_skill in DevOps:
    print(f"We Have {usr_skill} in DevOps Team.")
elif usr_skill in Development:
    print(f"We have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill.")
else:
    print("Skill not found")
    print("Please check if you have entered value in capitalize or check the spelling.")