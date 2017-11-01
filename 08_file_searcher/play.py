# RECURSION:
# def factorial(n):
#     if n == 1:
#         return 1
#
#     return n * factorial(n - 1)

# print('5!={:,}, 3!={:,}, 11!={:,}'.format(
#     factorial(5),  # 120
#     factorial(3),  # 6
#     factorial(11)  # HUGE
# ))


# GENERATORS:
# Fibonacci numbers:
# 1, 1, 2, 3, 5, 7, 13, 21, ...

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


print('Via lists')
for n in fibonacci(100):
    print(n, end=', ')
print()


def fibonacci_co(limit):
    current = 0
    next = 1

    # while current < limit:
    while True:
        current, next = next, next + current
        yield current


print('Via yield')
for n in fibonacci_co(100):
    if n > 10000:
        break
    print(n, end=', ')
