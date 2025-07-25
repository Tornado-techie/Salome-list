# Step 1: Create a list of words
words = ["boy", "girl", "mother", "father", "aunt", "uncle", "child"]

# Step 2: Use list comprehension to filter words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 == 1]

# Step 3: Print the result
print("Words with an odd number of characters:")
print(odd_length_words)
