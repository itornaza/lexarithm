#
# perfect.py
#

__all__ = ['is_perfect']

import math

def is_perfect(num):
    """
    Return True if num is a perfect number, False otherwise.
    A perfect number equals the sum of its proper divisors.
    """
    if not isinstance(num, int) or num <= 1: return False
    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_sum += i
            # Add the pair divisor if it's different
            if i != num // i and num // i != num:
                divisor_sum += num // i
    return divisor_sum == num

if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer to check if it's a perfect number: ").strip())
        if number <= 0:
            print("Please enter a positive integer.")
        elif is_perfect(number):
            print(f"Yes! {number} is a perfect number.")
            # Optional: show the divisors
            divisors = [1]
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    divisors.append(i)
                    if i != number // i and number // i != number:
                        divisors.append(number // i)
            print(f"Because 1 + {' + '.join(map(str, sorted(divisors[1:])))} = {number}")
        else:
            print(f"No, {number} is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")
        