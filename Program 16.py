# 4.1 Create and Access Dictionary Elements
print("---- Creating and Accessing Dictionary ----")
student = {
    "name": "Prashant",
    "age": 18,
    "course": "Computer Science"
}

# Access elements
print("Student Name:", student["name"])
print("Student Age:", student.get("age"))

# 4.2 Update Dictionary
print("\n---- Updating Dictionary ----")
student["grade"] = "A"      # Add new element
student["age"] = 19         # Update existing element

print("Updated Dictionary:", student)

# 4.3 Removing Elements
print("\n---- Removing Elements ----")
student.pop("course")       # Remove specific item
del student["grade"]        # Delete item
student.popitem()           # Remove last item

print("Dictionary after removal:", student)

# 4.4 Merging Dictionaries
print("\n---- Merging Dictionaries ----")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print("Merged using update():", dict1)

dict3 = {"x": 10, "y": 20}
dict4 = {"z": 30}

merged_dict = {**dict3, **dict4}
print("Merged using unpacking:", merged_dict)
