x = 13
y = 42
a = [y, y + x, y + 2 * x]

for k in a:
    print(k, "mod", x, "=", k % x)

print("och därmed är alla kongruenta i", x)