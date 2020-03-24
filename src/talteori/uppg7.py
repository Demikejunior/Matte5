x = 13
y = 42
a = [y, y + 13, y + 2 * 13]

for k in a:
    print(k, "mod", x, "=", k % x)

print("och därmed är alla kongruenta")