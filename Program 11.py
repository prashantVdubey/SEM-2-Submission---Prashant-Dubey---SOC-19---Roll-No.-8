# Experiment 11: File Handling

filename = 'sample.txt'

# 1. WRITE — Creates or overwrites the file
print('--- Writing to file ---')
with open(filename, 'w') as f:
    f.write('Hello, Python File Handling!\n')
    f.write('Line 2: Learning file operations.\n')
    f.write('Line 3: Writing data to disk.\n')
print('Data written successfully.')

# 2. READ — Read entire content
print('\n--- Reading entire file ---')
with open(filename, 'r') as f:
    content = f.read()
    print(content)

# 3. READ LINE BY LINE
print('--- Reading line by line ---')
with open(filename, 'r') as f:
    for i, line in enumerate(f, 1):
        print(f'  Line {i}: {line.rstrip()}')

# 4. APPEND — Add content without erasing
print('\n--- Appending to file ---')
with open(filename, 'a') as f:
    f.write('Line 4: Appended after opening again.\n')
    f.write('Line 5: File handling is easy!\n')
print('Data appended successfully.')

# 5. READ FINAL CONTENT
print('\n--- Final file content ---')
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')

print('\n--- File handling complete. File closed properly via with-block. ---')
