#
# highly-composite.py
#

import math
from collections import Counter

def count_divisors(n):
    """Return the number of divisors of n efficiently."""
    if n < 1:
        return 0
    count = 1
    # Handle factor 2
    exp = 0
    while n % 2 == 0:
        exp += 1
        n //= 2
    count *= (exp + 1)
    
    # Handle odd factors
    i = 3
    while i * i <= n:
        exp = 0
        while n % i == 0:
            exp += 1
            n //= i
        if exp > 0:
            count *= (exp + 1)
        i += 2
    
    if n > 1:
        count *= 2  # n is a prime greater than 2
    return count


def is_highly_composite(num):
    """
    Return True if num is highly composite:
    it has more divisors than every smaller positive integer.
    """
    if num < 1:
        return False

    # Special case: 1 is highly composite (by definition)
    if num == 1:
        return True

    # Check that for every k from 1 to num-1, d(k) < d(num)
    max_divisors_so_far = 0
    for k in range(1, num):
        divisors_k = count_divisors(k)
        if divisors_k > max_divisors_so_far:
            max_divisors_so_far = divisors_k
        if divisors_k >= count_divisors(num):
            return False

    return count_divisors(num) > max_divisors_so_far


if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer to check if it's highly composite: ").strip())

        if number < 1:
            print("Please enter a positive integer.")
        elif is_highly_composite(number):
            d = count_divisors(number)
            print(f"Yes! {number} is a HIGHLY COMPOSITE number.")
            print(f"It has {d} divisors — more than any smaller number!")
        else:
            print(f"No, {number} is not highly composite.")

    except ValueError:
        print("Please enter a valid positive integer.")
        