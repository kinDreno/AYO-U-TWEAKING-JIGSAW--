def count_vowels_and_consonants(input_string):
    # Initialize counts
    vowels_count = 0
    consonants_count = 0
    
    # Define vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    # Iterate through each character in the input string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:  # Check if it's a vowel
                vowels_count += 1
            else:  # It's a consonant
                consonants_count += 1

    # Return the counts in a dictionary
    return {
        "vowels": vowels_count,
        "consonants": consonants_count
    }

# Example usage
input_string = "Hello, World!"
result = count_vowels_and_consonants(input_string)
print(result)  # Output: {'vowels': 3, 'consonants': 7}
