#
# fibonacci.py
#

__all__ = ['is_fibonacci']

import math

def is_perfect_square(x):
    """Helper: returns True if x is a perfect square"""
    if x < 0: return False
    root = int(math.sqrt(x))
    return root * root == x

def is_fibonacci(num):
    """
    Return True if num is a Fibonacci number, False otherwise.
    Works for num >= 0
    """
    if not isinstance(num, int) or num < 0: return False
    return is_perfect_square(5 * num * num + 4) or \
           is_perfect_square(5 * num * num - 4)

if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer to check if it's a Fibonacci number: ").strip())
        if is_fibonacci(number):
            a, b = 0, 1
            position = 0
            while a < number:
                a, b = b, a + b
                position += 1
            if a == number:
                print(f"Yes! {number} is a Fibonacci number")
                if number == 0:
                    print("It's the 0th Fibonacci number")
                elif position == 1 or position == 2:
                    print("It's one of the 1st two Fibonacci numbers (F₁ = F₂ = 1)")
                else:
                    print(f"It's the {position}th Fibonacci number")
        else:
            print(f"No, {number} is not a Fibonacci number.")
    except ValueError:
        print("Please enter a valid integer.")
