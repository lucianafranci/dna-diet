def fibonacci_loop_child(months, offsprings):
    # offsprings = descendencia
    parrent, child = 1, 1
    for itr in range(months - 1):
        child, parrent = parrent, parrent + (child * offsprings)
    return child


print(fibonacci_loop_child(5, 2))
