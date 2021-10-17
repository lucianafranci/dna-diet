def fibonacci_loop(number):
    old = 1
    new = 1
    for itr in range(number - 1):
        tmpVal = new
        new = old
        old = old + tmpVal
    return new

# forma optimizada (pythonic)


def fibonacci_loop_new(number):
    old, new = 1, 1
    for itr in range(number - 1):
        new, old = old, old + new
    return new


print(fibonacci_loop(10))
print(fibonacci_loop_new(10))
