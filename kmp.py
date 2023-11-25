import time

def kmp(text, pattern):
    def build_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            lps[i] = j
        return lps

    positions = []
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    j = 0
    iterations = 0
    operations = 0
    for i in range(n):
        iterations += 1
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
            operations += 1  # Increment the operation count for lps lookup
        if text[i] == pattern[j]:
            j += 1
            operations += 1  # Increment the operation count for character comparison
        if j == m:
            positions.append(i - m + 1)
            j = lps[j - 1]
    operations += iterations  # One operation per iteration
    return positions, operations

def get_user_input():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    return text, pattern

text, pattern = get_user_input()

start_time_kmp = time.time()
kmp_positions, kmp_operations = kmp(text, pattern)
end_time_kmp = time.time()

kmp_execution_time = end_time_kmp - start_time_kmp
kmp_iterations = len(text) - len(pattern) + 1

print("\nEfficiency for KMP algorithm:")
print("Execution time:", kmp_execution_time, "seconds")
print("Number of operations:", kmp_operations)
