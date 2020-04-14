def a(n):
	return 2 ** (4 * n - 2) + 1

# uppg 10
print("a)")
print("	Defenition: a(n) = 2 ^ (4n - 2) + 1, n >= 1")
print("	a(1) =", a(1))
print("	Därmed bör faktorn (om det finns en gemensam faktor för alla a(n) där n >= 1) vara 5")
print()

print("b)")
print("	Bevis:")
print("	Om a(n) mod(5) = 0 för alla n >= 1 bör även (a(n + 1) - a(n)) mod(5) = 0")
print()
print("	a(n + 1) - a(n) = 2 ^ (4(n + 1) - 2) - 2 ^ (4n - 2) - 1 + 1 =")
print("	= 2 ^ (4n + 2) - 2 ^ (4n - 2) = 2 ^ (4n) * (4 - (1 / 4)) =")
print("	= 16 ^ (n) * (4 - (1 / 4)) = 16 ^ (n - 1) * (16 * 4 - 16 / 4) =")
print("	= 16 ^ (n - 1) * 60")
print()
print("	Därmed finns 60 som en faktor för skillnaden mellan alla a(n) där n >= 1,")
print("	vilket vidare medför att eftersom att a(1) är", a(1), "och att alla ökningar")
print("	därefter har 60 som en faktor kommer a(n) där n >= 1 alltid ha", a(1), "som en faktor")
