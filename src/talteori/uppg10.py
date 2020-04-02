def a(n):
	return 2 ** (4 * n - 2) + 1

# uppg 10
# a)

print("Defenition: a(n) = 2 ^ (4n - 2) + 1, n >= 1")
print("a(1) =", a(1))
print("Därmed bör faktorn (om det finns en gemensam faktor för alla a(n) där n >= 1) vara 5, då det är ett primtal")
print()

# b)

print("Bevis:")
print("Om a(n) mod(5) = 0 för alla n >= 1 bör även (a(n + 1) - a(n)) mod(5) = 0")
print()
print("a(n + 1) - a(n) = 2 ^ (4(n + 1) - 2) - 2 ^ (4n - 2) - 1 + 1 =")
print("= 2 ^ (4n + 2) - 2 ^ (4n - 2)")
