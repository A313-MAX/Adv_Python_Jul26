# Function to count the characters in a String.
def count_characters(text):
    frequency = {}

    # Convert string to lowercase
    text = text.lower()

    # Count only alphabetic characters
    for ch in text:
        if ch.isalpha():
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

    # Return dictionary in alphabetical order
    sorted_frequency = {}
    for key in sorted(frequency.keys()):
        sorted_frequency[key] = frequency[key]

    return sorted_frequency


# User input
text = input("Enter a string: ")

result = count_characters(text)
print("Character Frequency:", result)