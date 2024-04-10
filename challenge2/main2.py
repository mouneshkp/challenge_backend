import json
from collections import Counter
from typing import List, Tuple

def load_data(filename: str) -> List[int]:
    """Load a list of integers from a JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
        return data['numbers']

def calculate_frequency(numbers: List[int]) -> List[Tuple[int, int]]:
    """Calculate the frequency of each unique number and return sorted by frequency descending."""
    counter = Counter(numbers)
    sorted_frequency = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequency

def get_third_highest_frequency(frequencies: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Retrieve the third highest frequency from the list of (number, frequency) tuples."""
    if len(frequencies) < 3:
        raise ValueError("List has less than 3 unique numbers.")
    return frequencies[2]

def main():
    numbers = load_data('data.json')
    frequencies = calculate_frequency(numbers)
    
    try:
        third_highest_freq = get_third_highest_frequency(frequencies)
        print(f"Third highest frequency number: {third_highest_freq[0]}, Frequency: {third_highest_freq[1]}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
