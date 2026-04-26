# Create dictionary
student = {"b": 85, "a": 92, "c": 78}
# Sort by keys
print("Sorted by keys:")
for k in sorted(student):
    print(k, ":", student[k])
# Sort by values
print("\nSorted by values:")
for k, v in sorted(student.items(), key=lambda x: x[1]):
    print(k, ":", v)