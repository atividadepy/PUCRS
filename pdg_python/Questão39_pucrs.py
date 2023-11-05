def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

def generate_perfect_numbers():
    count = 0
    num = 2  # Começamos com o primeiro número perfeito conhecido

    while count < 5:
        if is_perfect_number(num):
            print(num)
            count += 1
        num += 1

if __name__ == "__main__":
    generate_perfect_numbers()
