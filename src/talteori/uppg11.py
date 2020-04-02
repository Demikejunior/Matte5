def formel1(n):
	out = 0
	for k in range(0, n + 1):
		out += k * (3 * k + 1)
	return out

def formel2(n):
	return n * ((n + 1) ** 2)

for n in range(0, 100):
	if formel1(n) == formel2(n):
		print("formel 1 av", n, "är lika med formel 2 av", n)
	else:
		print("formel 1 av", n, "är inte lika med formel 2 av", n)
	
	print()
