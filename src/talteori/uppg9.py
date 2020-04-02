def a(n):
	return 5 * (2 ** n)  - 3

print("Rekursiv formel def: a(0) = 2,")
print("a(n + 1) = 2a(n) + 3")
print()
print("Sluten formel def: a(n) = 5 * 2 ^ (n) - 3")
print("a(0) =", a(0))
print("a(n + 1) = 5 * 2 ^ (n + 1) - 3")
print()
print("Bevis att Rekursiv == Sluten:")
print("Rekursiv a(n+1) av Sluten a(n):")
print("2 * (5 * 2 ^ (n) - 3) + 3 =")
print("= 5 * 2 ^ (n + 1) - 6 + 3 =")
print("= 5 * 2 ^ (n + 1) - 6 = Sluten a(n+1)")
print("Q.E.D")
