#
# cube.py
#

__all__ = ['is_perfect_cube']

import math

def is_perfect_cube(num):
    """Pure integer method – most accurate for very large numbers."""
    if not isinstance(num, int):
        return False
    
    if num == 0:
        return True
    
    abs_num = abs(num)
    left, right = 0, abs_num
    
    while left <= right:
        mid = (left + right) // 2
        cube = mid * mid * mid
        
        if cube == abs_num:
            return True
        elif cube < abs_num:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

if __name__ == "__main__":
    try:
        number = int(input("Enter an integer to check if it's a perfect cube: ").strip())
        
        if is_perfect_cube(number):
            # Find the cube root
            root = round(abs(number) ** (1/3))
            if number < 0:
                root = -root
            print(f"Yes! {number} is a perfect cube.")
            print(f"→ {root}³ = {number}")
        else:
            print(f"No, {number} is not a perfect cube.")
            
    except ValueError:
        print("Please enter a valid integer.")