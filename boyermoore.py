import time

def boyer_moore(text, pattern):
    def bad_character_heuristic(pattern):
        """Creates a dictionary mapping each character in the pattern to the distance
        between its last occurrence and the end of the pattern."""
        bad_char_dict = {}
        for i, char in enumerate(pattern):
            bad_char_dict[char] = len(pattern) - i - 1
        return bad_char_dict

    def good_suffix_heuristic(pattern):
        """Creates a dictionary mapping each suffix of the pattern to the distance
        between the suffix and the end of the pattern."""
        good_suffix_dict = {}
        for i in range(len(pattern)):
            suffix = pattern[i:]
            for j in range(len(suffix) - 1, -1, -1):
                if suffix[j:] in good_suffix_dict:
                    good_suffix_dict[suffix] = j
                    break
            if suffix not in good_suffix_dict:
                good_suffix_dict[suffix] = len(suffix) - 1
        return good_suffix_dict

    def compute_shift(text, pattern, i, bad_char_dict, good_suffix_dict):
        """Computes the shift to be used for the next iteration."""
        shift = max(bad_char_dict.get(text[i], len(pattern)),
                    good_suffix_dict.get(pattern[i:], len(pattern)))
        return shift

    positions = []
    n, m = len(text), len(pattern)
    bad_char_dict = bad_character_heuristic(pattern)
    good_suffix_dict = good_suffix_heuristic(pattern)
    j = 0
    iterations = 0
    operations = 0
    for i in range(n):
        iterations += 1
        shift = compute_shift(text, pattern, i, bad_char_dict, good_suffix_dict)
        operations += 2  # Increment the operation count for bad character and good suffix checks
        j += shift
        if j == m:
            positions.append(i - m + 1)
            j = good_suffix_dict.get(pattern[j:], len(pattern))
    operations += iterations  # One operation per iteration
    return positions, operations

def get_user_input():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    return text, pattern

text, pattern = get_user_input()

start_time_bm = time.time()
bm_positions, bm_operations = boyer_moore(text, pattern)
end_time_bm = time.time()

bm_execution_time = end_time_bm - start_time_bm
bm_iterations = len(text) - len(pattern) + 1

print("\nEfficiency for Boyer-Moore algorithm:")
print("Execution time:", bm_execution_time, "seconds")
print("Number of operations:", bm_operations)
