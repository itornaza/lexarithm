#
# tester.py
#

__all__ = ['test_number']

import os
import sys

from prime import * # type : ignore
from perfect import * # type : ignore
from triangular import * # type : ignore
from square import * # type : ignore
from cube import * # type : ignore
from fibonacci import * # type : ignore
from factorial import * # type : ignore
from tetrahedral import * # type : ignore
from highly_composite import * # type : ignore

def test_number(num):
    """Run all special number tests on the given number."""

    # TODO: proper divisors, abundant/deficient, tetractys

    tests = [
        ("Prime",             is_prime),
        ("Perfect",           is_perfect),
        ("Triangular",        is_triangular),
        ("Perfect Square",    is_perfect_square),
        ("Perfect Cube",      is_perfect_cube),
        ("Fibonacci",         is_fibonacci),
        ("Factorial",         is_factorial),
        ("Tetrahedral",       is_tetrahedral),
        ("Highly Composite",  is_highly_composite),
    ]

    print(f"\nAnalyzing number: {num}\n")
    print("-" * 40)

    results = []
    yes_count = 0

    for name, func in tests:
        try:
            result = func(num)
        except Exception as e:
            result = False
            print(f"Error in {name}: {e}")
        status = "YES" if result else "no "
        if result:
            yes_count += 1
        results.append((name, result))
        print(f"{name:20} → {status}")

    print("-" * 40)
    print(f"\n{num} is special in {yes_count} way(s)!")

    if yes_count == 0:
        print("Just a regular number... but still loved")
    elif yes_count >= 4:
        print("This number is LEGENDARY!")
    elif yes_count >= 2:
        print("Pretty special!")

    info = prime_analysis(num)
    print("\nMore analysis \n")
    print(f"• Prime factors       : {' × '.join(map(str, info['prime_factors'])) or '—'}")
    print(f"• Proper divisors     : {', '.join(map(str, info['proper_divisors'])) or 'none'}")
    print(f"• Σ proper divisors   : {info['sum_of_proper_divisors']}")
    print(f"• Classification      : {info['abundance']}")
    
    return results

if __name__ == "__main__":
    while True:
        try:
            user_input = input("\nEnter a positive integer (or 'q' to quit): ").strip()
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("Goodbye!")
                break
            num = int(user_input)
            if num < 0:
                print("Please enter a non-negative integer.")
                continue
            test_number(num)
        except ValueError:
            print("Invalid input! Please enter a valid integer or 'q' to quit.")
        except KeyboardInterrupt:
            print("\n\nBye!")
            break
        