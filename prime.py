#
# prime.py 
#

__all__ = ['is_prime']

import math

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer to check if it's prime: "))
        if num < 0:
            print("Please enter a positive integer.")
        elif is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")