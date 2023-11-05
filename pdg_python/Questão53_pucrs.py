def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

def generate_primes(count):
    primes = [1, 2, 3]
    current_number = 5

    while len(primes) < count:
        if is_prime(current_number):
            primes.append(current_number)
        current_number += 2  # Primes greater than 2 are always odd

    return primes

# Calculate the first 20 prime numbers
first_20_primes = generate_primes(20)

# Print the result
print("The first 20 prime numbers are:")
print(first_20_primes)
