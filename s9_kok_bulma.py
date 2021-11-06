a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4 * a * c

x1 = (- b - delta ** 0.5) / (2 * a)
x2 = (- b + delta ** 0.5) / (2 * a)

print("denkleminin;\n1.koku: {}\n2. koku: {}".format(x1, x2))


# Kok almanin kolay yolu
import math
math.floor(delta)
