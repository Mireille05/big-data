def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]

def check_palindrome():
    text = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(text):
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

if __name__ == "__main__":
    check_palindrome()
