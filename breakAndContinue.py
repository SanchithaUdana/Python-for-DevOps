# Break Statement
import random

print("Break Statement")
for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my data.")
        break
print("Out of loop")

print()
print()
print("Continue Statement")
# Continue Statement
for i in "DevOps":
    if i == "O":
        print("Found my data.")
        continue
    print(f"Value of i is {i}")

print("Out of loop")

# example

VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"******TESTING VACCINE {vac}")
    if vac == LUCKY:
        print("###################################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("###################################")
        print()
        break
    print("XXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXX")
    print()
