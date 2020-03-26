import math


def isPowerOfPreviousFactor(factors, k):

	for i in range(0, len(factors)):

			if k % factors[i] == 0:

				return True
	
	return False


def a(input):
	return 2 ** (4 * input - 2)


def giveFactors(input):

	factors = []
	topRange = math.floor(math.sqrt(input) + 1)

	for k in range(2, topRange):

		if isPowerOfPreviousFactor(factors, k):
			break
		elif input % k == 0:
			factors.append(k)

	return factors


print(a(1), "har endast faktor", giveFactors(a(1)))
for n in range(2, 111):

	if giveFactors(a(n)).__contains__(giveFactors(a(1))[0]) == False:
		print(a(n), "har inte faktor", giveFactors(a(1)))
	else:
		print(a(n), "har endast faktor", giveFactors(a(1)))
