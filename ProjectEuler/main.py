def factorial(n):
    # return the factorial of n
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(sum([int(c) for c in str(factorial(100))]))
