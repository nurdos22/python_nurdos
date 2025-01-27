animals = ['cat', 'dog', 'rabbit']
fruits = ['apple', 'banana', 'orange', 'mango']

for animal in animals:
    print(animal)

for fruit in fruits:
    print(fruit)

# O(A + F)

print('----------------')
for animal in animals:
    for fruit in fruits:
        print(animal + ' loves ' + fruit)


# O(A * F)

# O (A + F + (A * F))

def counter(n):
    print(n)
    if (n > 0):
        counter(n - 1)

counter(3)