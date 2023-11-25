import time

def brute_force(text, pattern):
    positions = []
    n, m = len(text), len(pattern)
    start_time = time.time()
    operations = 0  # Initialize the operation count
    for i in range(n - m + 1):
        for j in range(m):
            operations += 1  # Increment the operation count for each character comparison
            if text[i + j] != pattern[j]:
                break
        else:
            positions.append(i)
    end_time = time.time()
    execution_time = end_time - start_time
    number_of_iterations = len(text) - len(pattern) + 1
    return positions, execution_time, number_of_iterations, operations

def get_user_input():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    return text, pattern

text, pattern = get_user_input()
positions, execution_time, number_of_iterations, bf_operations = brute_force(text, pattern)

print("Efficiency for Brute Force algorithm:")
print("Execution time:", execution_time, "seconds")
print("Number of operations:", bf_operations)
