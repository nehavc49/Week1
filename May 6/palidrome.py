def is_palindrome(text):
    # Reverse the text
    reversed_text = text[::-1]
    # Check if the original and reversed are the same
    if text == reversed_text:
        return True
    else:
        return False
# Get input from the user
word = input("Enter a word: ")
# Check and print result
if is_palindrome(word):
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")


