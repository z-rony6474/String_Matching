import time
import hashlib

def rabin_karp(text, pattern):
    """
    Implements the Rabin-Karp algorithm for finding occurrences of a pattern in a text.

    Args:
        text (str): The text to search for the pattern.
        pattern (str): The pattern to search for.

    Returns:
        list: A list of indices where the pattern occurs in the text.
        int: The number of operations performed.
    """

    # Calculate the hash value of the pattern
    d = 256
    pattern_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % d

    # Calculate the hash values of the first window of text
    h = 1
    for i in range(len(pattern)):
        h = (h * d) % d

    # Initialize the list of positions
    positions = []

    # Initialize the operation count
    operations = 0

    # Iterate over the text, sliding the window one character at a time
    for i in range(len(text) - len(pattern) + 1):
        # Calculate the hash value of the current window of text
        current_hash = 0
        for j in range(len(pattern)):
            current_hash = (d * current_hash + ord(text[i + j])) % d

        # Increment the operation count for calculating the hash value
        operations += len(pattern)

        # Check if the hash values match
        if current_hash == pattern_hash:
            # Do a character-by-character comparison to confirm the match
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    break

            # Increment the operation count for character comparisons
            operations += len(pattern)

            # If the character-by-character comparison matches, add the position to the list of positions
            if j == len(pattern) - 1:
                positions.append(i)

        # Calculate the hash value for the next window of text
        # Remove the leading digit, add the trailing digit
        if i < len(text) - len(pattern):
            current_hash = (current_hash + d * (ord(text[i + len(pattern)]) - ord(text[i])) ) % d

            # Increment the operation count for hash value updates
            operations += 2 * len(pattern)  # Two operations for each character update

    return positions, operations

def get_user_input():
    """
    Prompts the user to enter the text and pattern.

    Returns:
        tuple: A tuple containing the text and pattern.
    """

    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    return text, pattern

text, pattern = get_user_input()

start_time_rk = time.time()
rk_positions, rk_operations = rabin_karp(text, pattern)
end_time_rk = time.time()

rk_execution_time = end_time_rk - start_time_rk
rk_iterations = len(text) - len(pattern) + 1

print("\nEfficiency for Rabin-Karp algorithm:")
print("Execution time:", rk_execution_time, "seconds")
print("Number of operations:", rk_operations)
