# Experiment 3: Tuple Operations

# 1. Create and Access
colors = ('red', 'green', 'blue', 'yellow', 'purple')
print('Tuple:', colors)
print('First element:', colors[0])
print('Last element:', colors[-1])
print('Slice [1:3]:', colors[1:3])
print('Length:', len(colors))

# 2. Nested Tuple
nested = (('a', 'b', 'c'), (1, 2, 3), ('x', 'y', 'z'))
print('\nNested Tuple:', nested)
print('Access nested[1][2]:', nested[1][2])
print('Access nested[0]:', nested[0])

# 3. Repetition
nums = (1, 2, 3)
repeated = nums * 3
print('\nOriginal:', nums)
print('Repeated (x3):', repeated)

# 4. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)
combined = tuple1 + tuple2 + tuple3
print('\nTuple1:', tuple1)
print('Tuple2:', tuple2)
print('Tuple3:', tuple3)
print('Concatenated:', combined)
