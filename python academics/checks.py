def count_vowels_and_consonants(input_string):
    vowels_count = 0
    consonants_count = 0
    vowels = "aeiouAEIOU"
    
    for char in input_string:
        if char.isalpha():  
            if char in vowels:
                vowels_count += 1
            else: 
                consonants_count += 1

    return {
        "vowels": vowels_count,
        "consonants": consonants_count
    }

result = count_vowels_and_consonants("hellow")
print(result) 
