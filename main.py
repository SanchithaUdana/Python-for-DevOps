import mathModule
from mathModule import *

print("All the methods including in mathModule module")
print(dir(mathModule))

# type 01 to use module
print("Step 01")
print("########")

ans1 = mathModule.multiply_numbers(12, 45)
ans2 = mathModule.sum_numbers(12, 45)
ans3 = mathModule.divide_numbers(12, 45)

print(ans1)
print(ans2)
print(ans3)


# type 2 to use module
print("Step 02")
print("########")

print(sum_numbers(12, 45))
print(divide_numbers(12, 45))
print(multiply_numbers(12, 45))

