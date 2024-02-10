def count_words(sentence):
    # Split the sentence into words using the split() method
    words = sentence.split()

    # Count the number of words
    word_count = len(words)

    return word_count

def main():
    print("Welcome to the Word Counter program!")
    
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")

    # Check if the user provided any input
    if user_input.strip():
        # Call the count_words function to get the word count
        result = count_words(user_input)

        # Display the word count
        print(f"\nWord Count: {result}")
    else:
        print("You didn't enter any text. Please try again.")

if __name__ == "__main__":
    main()

