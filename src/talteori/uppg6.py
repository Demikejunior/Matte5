x = 17
y = 5
a = []

for k in range(2, 10):
    print(x, "mod", k, "=", x % k)
    print(y, "mod", k, "=", y % k)
    if (x % k == y % k):
        a.append(k)

for k in a:
    print(x, "och", y, "är kongruent i", k)