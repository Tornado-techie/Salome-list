# Step 1: Create an empty list
my_list = []

# Step 2: Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert value 15 at the second position in the list
my_list.insert(1, 15)

# Step 4: Extend list with another list
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from the list
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of value 30 in the list
index_of_30 = my_list.index(30)
print("Final list:", my_list)
print(f"The index of 30 is: {index_of_30}")
