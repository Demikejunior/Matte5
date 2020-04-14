def prog(n, am, m, d):
    return am + (n - m) * d

#Uppgift 12
# a)
print("a)")
print("a100 =", prog(100, 8, 2, 4))
print()

# b)
print("b)")
print("an = 4n")
print()

#13
# a)
print("a)")
print(prog(5, 10, 4, (40 - 10) / 2))
print()

# b)
print("b)")
print(prog(16, 10, 4, 15))
