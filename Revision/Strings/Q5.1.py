count_vowels = "Coding in Python is fun and fun"

vowel_count = sum(count_vowels.lower().count(vowel) for vowel in "aeiou")
print(vowel_count)