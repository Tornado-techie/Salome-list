# Ask user to input the first set of numbers
input1 = input("Enter numbers for the first set (separated by spaces): ")
set1 = set(map(int, input1.split()))

# Ask user to input the second set of numbers
input2 = input("Enter numbers for the second set (separated by spaces): ")
set2 = set(map(int, input2.split()))

# Find the common elements
common_elements = set1 & set2  # or use set1.intersection(set2)

# Print the result
print("\nCommon elements in both sets:")
print(common_elements)
