#
# triangular.py
#

__all__ = ['is_triangular']

import math

def is_triangular(num):
    """
    Return True if num is a triangular number (n*(n+1)/2 for some integer n >= 0),
    otherwise False.
    """
    if not isinstance(num, int) or num < 0:
        return False
    
    if num == 0 or num == 1:
        return True  # 0! and 1st triangular numbers
    
    # Solve the equation: n(n+1)/2 = num → n² + n - 2*num = 0
    # Use quadratic formula: n = [-1 ± sqrt(1 + 8*num)] / 2
    # We take the positive root: n = [-1 + sqrt(1 + 8*num)] / 2
    discriminant = 1 + 8 * num
    sqrt_disc = math.sqrt(discriminant)
    
    # Check if discriminant is a perfect square and n is integer
    if sqrt_disc == int(sqrt_disc):
        n = (-1 + int(sqrt_disc)) // 2
        return n * (n + 1) // 2 == num  # Extra safety check
    
    return False


if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer to check if it's triangular: "))
        
        if is_triangular(number):
            # Find which triangular number it is
            discriminant = 1 + 8 * number
            n = int(math.sqrt(discriminant))
            n = (-1 + n) // 2
            print(f"Yes! {number} is the {n}th triangular number: {n}×{n+1}/2 = {number}")
        else:
            print(f"No, {number} is not a triangular number.")
            
    except ValueError:
        print("Please enter a valid integer.")