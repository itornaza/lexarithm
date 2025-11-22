#
# tetrahedral.py
#

__all__ = ['is_tetrahedral']

import math

def is_tetrahedral(num):
    """
    Return True if num is a tetrahedral number, i.e.,
    there exists an integer n >= 0 such that n(n+1)(n+2)/6 = num
    """
    if not isinstance(num, int) or num < 0: return False
    if num == 0: return True  # 0th tetrahedral number (by convention)

    # Solve the equation: n(n+1)(n+2) = 6 * num
    # We solve the cubic equation using the inverse formula
    # n ≈ cube root of (6*num) → but we use exact integer method
    n = 1
    while True:
        tetrahedral = n * (n + 1) * (n + 2) // 6
        if tetrahedral == num:
            return True
        if tetrahedral > num:
            return False
        n += 1

if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer to check if it's tetrahedral: ").strip())
        if is_tetrahedral(number):
            # Find which tetrahedral number it is
            n = 1
            while n * (n + 1) * (n + 2) // 6 != number:
                n += 1
            print(f"Yes! {number} is the {n}th tetrahedral number")
            print(f"Formula: {n}×{n+1}×{n+2}/6 = {number}")
        else:
            print(f"No, {number} is not a tetrahedral number.")
    except ValueError:
        print("Please enter a valid integer.")
        