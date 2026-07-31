def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in input_string if char in vowels)

input_string = "Hello"
vowel_count = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is {vowel_count}.")

