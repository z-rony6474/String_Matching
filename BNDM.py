import time

def initialize_bad_character_table(pattern):
    m = len(pattern)
    bad_char = {}

    for i in range(m - 1):
        bad_char[pattern[i]] = m - i - 1

    return bad_char

def BNDM(text, pattern):
    positions = []
    n, m = len(text), len(pattern)
    start_time = time.time()
    operations = 0  # Initialize the operation count

    bad_char = initialize_bad_character_table(pattern)
    shift = 0

    while shift <= n - m:
        j = m - 1
        i = shift + m - 1
        operations += 1  # Increment the operation count for each character comparison

        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
            operations += 1

        if j == -1:
            positions.append(shift)

        if j < m - 1:
            shift += max(1, m - 1 - j)
        else:
            shift += 1

    end_time = time.time()
    execution_time = end_time - start_time
    number_of_iterations = len(text) - len(pattern) + 1

    return positions, execution_time, number_of_iterations, operations

def get_user_input():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    return text, pattern

text, pattern = get_user_input()
positions, execution_time, number_of_iterations, bndm_operations = BNDM(text, pattern)

print("Efficiency for BNDM algorithm:")
print("Execution time:", execution_time, "seconds")
print("Number of operations:", bndm_operations)
