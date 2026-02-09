def check_prime(num1):
    for n in range(num1-1):
        if num1 % n == 0:
            return True
        