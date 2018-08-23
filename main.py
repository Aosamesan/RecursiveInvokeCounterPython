from RecursiveCounter import *


def euclidean_algorithm(invoker, a, b):
    m = max(a, b)
    n = min(a, b)
    s = m % n
    if s == 0:
        return n
    else:
        return invoker.invoke(n, s)

r = RecursiveCounter.create_recursive_counter(euclidean_algorithm)
# 15, 24 (1) / 9, 15 (2) / 6, 9 (3) / 3, 6 (4) => GCD 3, count 4
v = r.invoke(15, 24)

print("{0}, {1}".format(v, r.get_count()))
