#!/usr/bin/env python3
"""
Script to find and check even numbers divisible by 6 and 8.
Numbers divisible by both 6 and 8 must be divisible by their LCM (24).
"""

def is_divisible_by_6_and_8(num):
    """Check if a number is even and divisible by both 6 and 8."""
    return num % 2 == 0 and num % 6 == 0 and num % 8 == 0


def find_divisible_in_range(start, end):
    """Find all numbers divisible by 6 and 8 in a given range."""
    result = [num for num in range(start, end + 1) if is_divisible_by_6_and_8(num)]
    return result


def main():
    print("=== Even Numbers Divisible by 6 and 8 ===\n")
    
    # Test individual numbers
    test_numbers = [12, 24, 36, 48, 60, 72, 84, 96]
    print("Testing individual numbers:")
    for num in test_numbers:
        is_valid = is_divisible_by_6_and_8(num)
        print(f"{num}: {is_valid}")
    
    print("\n" + "="*40 + "\n")
    
    # Find numbers in a range
    print("Numbers divisible by both 6 and 8 in range [1, 100]:")
    numbers = find_divisible_in_range(1, 100)
    print(numbers)
    
    print("\n" + "="*40 + "\n")
    
    # Interactive mode
    while True:
        try:
            user_input = input("Enter a number to check (or 'q' to quit): ").strip()
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            
            num = int(user_input)
            if is_divisible_by_6_and_8(num):
                print(f"✓ {num} is even and divisible by both 6 and 8")
            else:
                print(f"✗ {num} is NOT divisible by both 6 and 8")
        except ValueError:
            print("Please enter a valid integer or 'q' to quit.")


if __name__ == "__main__":
    main()
