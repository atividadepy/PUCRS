def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def main():
    start = 92
    end = 1478
    product = 1

    for num in range(start, end + 1):
        if is_prime(num):
            product *= num

    print("Produto dos números primos entre 92 e 1478:", product)

if __name__ == "__main__":
    main()