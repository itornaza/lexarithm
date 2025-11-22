#
# prime.py 
#

__all__ = ['is_prime', 'format_factors', 'prime_analysis']

import math

def prime_factors(n: int) -> list[int]:
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    factors = prime_factors(n)
    return len(factors) == 1 and factors[0] == n

def format_factors(n: int) -> str:
    factors = prime_factors(n)
    if len(factors) == 1 and factors[0] == n:
        return f"{n} (prime)"
    from collections import Counter
    return " × ".join(f"{p}^{e}" if e > 1 else str(p)
                      for p, e in Counter(factors).items())

def prime_analysis(n: int):
    """One function to rule them all"""
    if n < 2:
        return {
            "prime_factors": [],
            "proper_divisors": [],
            "sum_of_proper_divisors": [],
            "abundance": "n/a"
        }

    factors = []
    divisors = {1}

    # Trial division
    temp = n
    i = 2
    while i * i <= temp:
        while temp % i == 0:
            factors.append(i)
            divisors.add(i)
            temp //= i
        i += 1 if i == 2 else 2  # skip evens after 2

    if temp > 1:
        factors.append(temp)
        divisors.add(temp)

    divisors.discard(n)                    # remove n itself → proper divisors
    proper_sum = sum(divisors)
    all_divs = sorted(divisors | {n})      # add n back for full list

    return {
        "prime_factors": factors,
        "proper_divisors": sorted(divisors),
        "sum_of_proper_divisors": proper_sum,
        "abundance": "Perfect" if proper_sum == n else
                     "Abundant" if proper_sum > n else
                     "Deficient"
    }

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
