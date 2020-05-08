i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
    
print('-----')

def loop(j):
    i = 0
    numbers = []
    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)
    
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers
        
a = loop(3)
print(a)
print('-----')
b = loop(5)
print(b)