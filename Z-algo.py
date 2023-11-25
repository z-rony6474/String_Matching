import time

def z_algorithm(text, pattern):
    concat = pattern + "$" + text
    n = len(concat)

    # Initialize Z array with zeros
    z = [0] * n

    # Initialize the Z-box boundaries
    l, r = 0, 0

    start_time = time.time()
    operations = 0  # Initialize the operation count

    for i in range(1, n):
        operations += 1  # Increment the operation count for each character comparison
        if i <= r:
            # Case 1: i lies within the current Z-box
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                # Check the remaining characters
                j = r + 1
                while j < n and concat[j - i] == concat[j]:
                    operations += 1  # Increment the operation count for each character comparison
                    j += 1
                z[i] = j - i
                l, r = i, j - 1
        else:
            # Case 2: i is outside the current Z-box
            j = 0
            while i + j < n and concat[j] == concat[i + j]:
                operations += 1  # Increment the operation count for each character comparison
                j += 1
            z[i] = j
            if j > 0:
                l, r = i, i + j - 1

    end_time = time.time()
    execution_time = end_time - start_time

    # Find occurrences of the pattern in the text
    occurrences = [i - len(pattern) - 1 for i in range(n) if z[i] == len(pattern)]

    return occurrences, execution_time, operations

def get_user_input():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    return text, pattern

text, pattern = get_user_input()
positions, execution_time, z_operations = z_algorithm(text, pattern)

print("\nEfficiency for Z algorithm:")
print("Pattern found at positions:", positions)
print("Execution time:", execution_time, "seconds")
print("Number of operations:", z_operations)
