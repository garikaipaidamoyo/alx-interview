#!/usr/bin/python3


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def remove_multiples(nums, prime):
    return [num for num in nums if num % prime != 0]


def isWinner(x, nums):
    ben_wins = 0
    maria_wins = 0

    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]

        while primes:
            ben_turn = True

            for prime in primes:
                if ben_turn:
                    ben_wins += 1
                    primes = remove_multiples(primes, prime)
                else:
                    maria_wins += 1
                    primes = remove_multiples(primes, prime)

                ben_turn = not ben_turn

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


# Testing the  function
print("Winner:", isWinner(3, [4, 5, 1]))
