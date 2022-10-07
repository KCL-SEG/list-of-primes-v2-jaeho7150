"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    current_num = 1
    if number_of_primes < 1:
        raise ValueError("Input number should be greater than 0")

    while len(list) < number_of_primes:
        if current_num > 1:
            for i in range(2,current_num):
                if (current_num % i) == 0:
                    break
            else:
                list.append(current_num)


        current_num += 1

    return list
