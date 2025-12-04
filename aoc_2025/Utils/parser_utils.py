from typing import Tuple, List, Union
from itertools import combinations  # Added for the new function


def parse_number_string(input_str: str) -> Tuple[int, ...]:
    """
    Analyzes a string containing numbers to determine the appropriate separator,
    and returns a tuple of integers.

    It tests for common separators (comma, space) and defaults to treating
    each character as a separate digit if no separator is found.

    Args:
        input_str: The string containing numbers.

    Returns:
        A tuple of integers parsed from the string.

    Raises:
        ValueError: If a non-numeric character is found in the input string
                    when parsing as individual digits.
    """

    # 1. Strip whitespace just in case
    clean_str = input_str.strip()

    if not clean_str:
        return tuple()

    # --- Strategy 1: Check for Comma Separator ---
    if "," in clean_str:
        # Assuming comma is the primary separator
        try:
            # Split by comma, then convert to integer, ignoring empty strings
            return tuple(int(n.strip()) for n in clean_str.split(",") if n.strip())
        except ValueError:
            # If conversion fails, it might be a mix-up, fall through to default check
            pass

    # --- Strategy 2: Check for Space Separator ---
    if " " in clean_str:
        # Assuming space is the primary separator
        try:
            # Split by space, then convert to integer, ignoring empty strings
            return tuple(int(n.strip()) for n in clean_str.split(" ") if n.strip())
        except ValueError:
            # If conversion fails, fall through to default check
            pass

    # --- Strategy 3: No Separator (Treat as individual digits) ---
    # This is the default if the above checks fail or no separator is present.

    # Check if the string contains only digits before attempting to split it
    # into individual characters. This prevents errors if a word was passed.
    if not clean_str.isdigit():
        # Raise an error if the string contains non-digit characters AND no
        # expected separator was found.
        raise ValueError(
            f"Input string '{input_str}' contains non-numeric characters and no recognized separator (',', ' ')."
        )

    # Split into individual characters and convert them to integers
    return tuple(int(digit) for digit in clean_str)


# ----------------------------------------------------------------------
# NEW FUNCTION ADDED
# ----------------------------------------------------------------------
def find_highest_two_digit_number_from_combinations(
    int_tuple: Tuple[int, ...],
) -> Union[int, None]:
    """
    Finds the highest two-digit number that can be formed by taking
    combinations of two digits from the input tuple, preserving their
    original relative order.

    The combination (a, b) forms the number a * 10 + b.

    Args:
        int_tuple: A tuple of integers (single digits recommended, but works with any).

    Returns:
        The highest two-digit number formed, or None if the tuple has fewer than 2 elements.
    """
    if len(int_tuple) < 2:
        return None

    # Use itertools.combinations to get all unique pairs (a, b) while preserving order.
    # The generator expression forms the number (a * 10 + b) for each pair.
    generated_numbers = (a * 10 + b for a, b in combinations(int_tuple, 2))

    # Find the maximum value from the generated numbers
    # If the tuple contains non-single digits (e.g., (10, 5)),
    # the resulting number will be > 99 (e.g., 10 * 10 + 5 = 105).
    # This is fine as the function is designed to find the maximum possible number.
    return max(generated_numbers)


def sum_tuple_of_ints(int_tuple: Tuple[int, ...]) -> int:
    """
    Calculates the sum of all integers in a given tuple.

    Args:
        int_tuple: The tuple of integers.

    Returns:
        The total sum of the elements.
    """
    return sum(int_tuple)


# ----------------------------------------------------------------------


# Example usage (for testing purposes)
if __name__ == "__main__":
    # Test cases for parse_number_string
    test_cases = [
        ("123456789", "No separator"),
        ("1,2,3,45,67", "Comma separator"),
        ("10 20 30 40", "Space separator"),
        ("  5 6 7 ", "Space separator with padding"),
        ("90,80,70,", "Comma separator with trailing comma"),
        ("100", "Single number, no separator"),
        ("", "Empty string"),
        (" 1 2, 3 4 ", "Mixed separators (will use space first)"),
    ]

    print("--- Running Parsing and Sum Test Cases ---")
    for s, desc in test_cases:
        try:
            result = parse_number_string(s)
            print(f"Input: '{s}' ({desc}) -> Tuple: {result}")

            # Use the sum function
            total = sum_tuple_of_ints(result)
            print(f"  Sum: {total}")

        except ValueError as e:
            print(f"Input: '{s}' ({desc}) -> Error: {e}")

    # Example of a case that should fail
    print("\n--- Running Failure Case ---")
    try:
        parse_number_string("12A34")
    except ValueError as e:
        print(f"Input: '12A34' -> Caught Error: {e}")

    # --- Running Combination Tests for the New Function ---
    print("\n--- Running Combination Tests ---")

    # Simple test case: Max number is 98 formed by (9, 8)
    simple_input = "1928"
    simple_tuple = parse_number_string(simple_input)
    max_num = find_highest_two_digit_number_from_combinations(simple_tuple)
    print(
        f"Input: '{simple_input}' (Tuple: {simple_tuple}) -> Max Combination: {max_num}"
    )

    # Large test case: Max number is 99 formed by (9, 9)
    large_input = "918293"
    large_tuple = parse_number_string(large_input)
    max_num = find_highest_two_digit_number_from_combinations(large_tuple)
    print(
        f"Input: '{large_input}' (Tuple: {large_tuple}) -> Max Combination: {max_num}"
    )

    # Test with very long number (from previous query in history)
    original_long_number = "2555245573282137352766682525526364435746545343523394355638332326665366122245646523573255525564158774"
    original_tuple = parse_number_string(original_long_number)
    max_original = find_highest_two_digit_number_from_combinations(original_tuple)
    print(
        f"Input: (Original Long Number) -> Max Combination: {max_original}"
    )  # Max is 99

    # Short test cases
    print(
        f"Input: (1, 2) -> Max Combination: {find_highest_two_digit_number_from_combinations((1, 2))}"
    )
    print(
        f"Input: (9,) -> Max Combination: {find_highest_two_digit_number_from_combinations((9,))}"
    )
