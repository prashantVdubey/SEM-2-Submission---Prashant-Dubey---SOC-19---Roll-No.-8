# 1. Create and Access
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print('Original List:', fruits)
print('First element:', fruits[0])
print('Last element:', fruits[-1])
print('Slice [1:3]:', fruits[1:3])

# 2. Add Elements
fruits.append('fig')          # Add at end
fruits.insert(2, 'blueberry') # Add at index 2
print('\nAfter adding elements:', fruits)

# 3. Remove Elements
fruits.remove('date')         # Remove by value
popped = fruits.pop()         # Remove last element
print('Popped element:', popped)
print('After removing elements:', fruits)

# 4. Sort
fruits.sort()
print('\nSorted List:', fruits)

# 5. Reverse
fruits.reverse()
print('Reversed List:', fruits)
