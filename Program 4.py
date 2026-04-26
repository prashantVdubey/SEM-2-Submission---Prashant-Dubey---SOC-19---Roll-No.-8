# Experiment 4: Dictionary Operations

# 1. Create and Access
student = {
    'name': 'Alice',
    'age': 21,
    'marks': 95,
    'course': 'Computer Science'
}
print('Dictionary:', student)
print('Name:', student['name'])
print('Marks:', student.get('marks'))
print('Keys:', list(student.keys()))
print('Values:', list(student.values()))

# 2. Update Dictionary
student['age'] = 22
student['grade'] = 'A+'
print('\nAfter Update:', student)

# 3. Removing Elements
removed = student.pop('marks')
print('\nRemoved marks value:', removed)
del student['course']
print('After Removals:', student)

# 4. Merging Dictionaries
extra = {'email': 'alice@example.com', 'city': 'Mumbai'}
merged = {**student, **extra}
print('\nMerged Dictionary:', merged)
