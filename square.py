#
# square.py
#

__all__ = ['is_perfect_square']

import math

def is_perfect_square(num):
    if not isinstance(num, int) or num < 0:
        return False
    if num == 0 or num == 1:
        return True
    
    left, right = 1,  num // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer to check if it's a perfect square: "))
        
        if is_perfect_square(number):
            root = int(math.sqrt(number))
            print(f"Yes! {number} is a perfect square: {root}² = {number}")
        else:
            print(f"No, {number} is not a perfect square.")
            
    except ValueError:
        print("Please enter a valid integer.")