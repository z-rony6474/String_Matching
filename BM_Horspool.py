# This request needs following APIs from available ones: text-code
# I already know API descriptions for all of them.
import time

def boyer_moore_horspool(text, pattern):
    """
    Implements the Boyer-Moore-Horspool algorithm for finding occurrences of a pattern in a text.

    Args:
        text (str): The text to search for the pattern.
        pattern (str): The pattern to search for.

    Returns:
        list: A list of indices where the pattern occurs in the text.
    """

    # Calculate the bad character shift table
    bad_character_shift = {}
    for i in range(len(pattern) - 1):
        bad_character_shift[pattern[i]] = len(pattern) - i - 1

    # Start the search at the beginning of the text
    i = 0
    operation_count = 0
    while i < len(text) - len(pattern) + 1:
        operation_count += 1
        # Compare the pattern to the text starting at the current position
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            operation_count += 1
            j -= 1

        # If the pattern matches the text, return the current position
        if j == -1:
            return i,operation_count

        # Otherwise, skip to the next position based on the bad character shift table
        i += bad_character_shift.get(text[i + len(pattern) - 1], len(pattern))

    # If the pattern is not found, return None
    return None,operation_count

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
    positions,operation_count = boyer_moore_horspool(text, pattern)
    end_time = time.time()

    execution_time = end_time - start_time

    print("Execution time:", execution_time, "seconds")
    print("Number of operations: ",operation_count)

if __name__ == "__main__":
    main()
