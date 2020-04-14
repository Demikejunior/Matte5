def formel1(n):
	out = 0
	for k in range(0, n + 1):
		out += k * (3 * k + 1)
	return out

def formel2(n):
	return n * ((n + 1) ** 2)

