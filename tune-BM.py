# This request needs following APIs from available ones: text-code
# I already know API descriptions for all of them.
import time

def tuned_boyer_moore(text, pattern):

    # Calculate the bad character shift function
    bad_character_shift = {}
    for i in range(len(pattern) - 1):
        bad_character_shift[pattern[i]] = len(pattern) - i - 1

    # Calculate the good suffix shift function
    good_suffix_shift = [len(pattern) + 1] * len(pattern)

    for i in range(len(pattern) - 2, -1, -1):
        j = good_suffix_shift[i + 1]
        while j < len(pattern) and pattern[i] == pattern[len(pattern) - j - 1]:
            j += 1

        good_suffix_shift[i] = j

    # Search for the pattern in the text
    positions = []
    i = 0
    operation_count = 0
    while i < len(text) - len(pattern) + 1:
        operation_count += 1
        # Compare the pattern to the text starting at the current position
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            operation_count += 1
            j -= 1

        # If the pattern matches the text, add the current position to the list of positions
        if j == -1:
            positions.append(i)

        # Calculate the next position to try
        shift = max(bad_character_shift.get(text[i + len(pattern) - 1], len(pattern)), good_suffix_shift[j])

        i += shift

    return positions, operation_count

def get_user_input():
    """
    Prompts the user to enter the text and pattern.

    Returns:
        tuple: A tuple containing the text and pattern.
    """

    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    return text, pattern

def main():

    text, pattern = get_user_input()
    start_time = time.time()
    positions, operation_count = tuned_boyer_moore(text, pattern)
    end_time = time.time()

    execution_time = end_time - start_time

    if positions:
        print("The pattern occurs at the following positions:")
        for position in positions:
            print(position)
    else:
        print("The pattern does not occur in the text.")

    print("Execution time:", execution_time, "seconds")
    print("Number of operations:", operation_count)

if __name__ == "__main__":
    main()
