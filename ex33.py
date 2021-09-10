i = 0
numbers = []

'''
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
'''
'''
def test(i, end, increment):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + increment
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

    if i < end:
        test(i, end, increment)

test(0,6,1)

print("The numbers: ")

for num in numbers:
    print(num)
'''

for i in range(0,6):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
