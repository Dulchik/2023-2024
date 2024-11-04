from collections import Counter

def find_max_occurrence(numbers):
    # Use Counter to count occurrences of each number
    counter = Counter(numbers)

    # Find the number with the maximum occurrence
    max_occurrence = counter.most_common(1)[0]

    return max_occurrence

# Example usage
numbers_list = [1, 2, 3, 4, 2, 2, 3, 4, 5, 5, 5, 5]
result = find_max_occurrence(numbers_list)

number_with_max_occurrence = result[0]
max_occurrence_count = result[1]

print(f"The number with the maximum occurrence is {number_with_max_occurrence} with {max_occurrence_count} occurrences.")
