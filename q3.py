def combine_and_iterate():
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")
    combined_text = text1 + text2
    char_list = list(combined_text)
    print("List of characters from the combined text:", char_list)
    print("Thank you for using my application\nafter processing the input.")
    return char_list

# Run the function
combine_and_iterate()