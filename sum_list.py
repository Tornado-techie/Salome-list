# Ask the user to enter numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string into parts and convert each to an integer
numbers = list(map(int, user_input.split()))

# Compute the sum of the list
total = sum(numbers)

# Print the result
print(f"The sum of the numbers is: {total}")
