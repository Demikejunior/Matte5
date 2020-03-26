def rec1(n):
    return 5 * (2 ** n)  - 3

def rec2(n):
    return 2 * n + 3

for n in range(0, 10):
    print("Formel ett av", rec1(n - 1), "=", rec1(n))
    print("Formel två av", rec1(n-1), "=", rec2(rec1(n - 1)))
    print()
