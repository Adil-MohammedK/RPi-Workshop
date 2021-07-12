import random
num=1

# while num>=1:
#     print(num)
#     num=num+1

# Printing 1 to 19
# for x in range(1,20): 
#     print (x)

# Printing number triangle
# for x in range(1,6):
#     for y in range(1,x+1):
#         print("*", end=" ")
#     print("")

# Throwing two dice
for x in range(1,11):
    throw_1=random.randint(1,6)
    throw_2=random.randint(1,6)
    total=throw_1+throw_2
    print(total)
    if total == 7:
        print("Seven thrown")
    if total == 11:
        print("Eleven thrown")
    if throw_1 == throw_2:
        print("Double thrown")

a=total
if a>7:
    print("a is big")
else:
    print("a is small")

if a>10:
    print("a is very big")
elif a>7:
    print("a is big")
else:
    print("a is small")