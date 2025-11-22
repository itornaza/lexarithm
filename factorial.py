#
# factorial.py
#

__all__ = ['is_factorial']

import math

def is_factorial(num):
    """
    Return True if num is a factorial (n! for some integer n >= 0),
    otherwise False.
    """
    if not isinstance(num, int) or num < 0: return False
    if num == 1: return True
    
    # Start from n = 1 and keep multiplying until we reach or exceed num
    factorial = 1
    n = 1    
    while factorial < num:
        n += 1
        factorial *= n
        
        # If we exactly match, it's a factorial
        if factorial == num:
            return True
            
        # Early exit if factorial becomes larger than num
        if factorial > num:
            return False
    
    return False


if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer to check if it's a factorial: "))
        if is_factorial(number):
            fact = 1
            n = 0
            while fact != number:
                n += 1
                fact *= n
            print(f"Yes! {number} = {n}!")
        else:
            print(f"No, {number} is not a factorial of any integer.")
    except ValueError:
        print("Please enter a valid positive integer.")
        