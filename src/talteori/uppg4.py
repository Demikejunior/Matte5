def aNPlusOne(aN):
    return 2 * aN - 4

aN = [3]
print(aN[0])
for i in range(1, 5):
    aN.append(aNPlusOne(aN[i - 1]))
    print(aN[i - 1], "ggr 2 - 4 =", aN[i])