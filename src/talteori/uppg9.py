def rec1(n):
    return 5 * (2 ** n)  - 3

def rec2(n):
    return 2 * n + 3

for n in range(0, 10):
    print(rec1(n), rec2(rec1(n - 1)))
