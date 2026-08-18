def convert(text):
    return "-".join(text.split())

print(convert("Hello I am good"))
# Import the 're' module, which is used for Regular Expressions
import re

# Define a function named 'convert' that takes 'text' as input
def convert(text):

    # re.sub() searches for a pattern and replaces it with the given replacement
    # r"\s+" means: find one or more whitespace characters (spaces, tabs, etc.)
    # "-" is what we want to replace those spaces with
    # 'text' is the string in which we want to make the replacement
    return re.sub(r"\s+", "-", text)


# Ask the user to enter a sentence and store it in the variable 'text'
text = input("Enter text: ")

# Call the convert() function, pass 'text' to it, and print the returned result
print(convert(text))