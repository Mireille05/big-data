def check_palindrome():
    text = input("Enter a string to check if it's a palindrome: ")
    cleaned_text = text.lower().replace(" ", "")  # Optional: remove spaces for better check
    if cleaned_text == cleaned_text[::-1]:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

# Run the function
check_palindrome()
