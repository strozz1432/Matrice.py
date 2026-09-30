import math


class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def det(self):
        return self.a * self.d - self.b * self.c

    def aigenval(self):
        t = self.a + self.d
        det = self.det()
        disc = t**2 - 4 * det

        if disc < 0:
            return []
        r = math.sqrt(disc)
        return [
            (t + r) / 2,
            (t - r) / 2
        ]

    def aigenvec(self, val):
        a = self.a - val
        b = self.b
        c = self.c
        d = self.d - val

        if abs(a) > abs(b):
            return ((b, -a))

        return (-d, c)

    def aigenvecs(self):
        return [(v, self.aigenvec(v)) for v in self.aigenval()]

    def scaledaigenvecs(self):
        vals = [self.aigenvec(v) for v in self.aigenval()]
        scaled = []

        for vec in vals:
            scale = math.gcd(int(vec[0]), int(vec[1]))
            if scale == 0:
                scaled.append(vec)
            else:
                scaled.append(tuple(x / scale for x in vec))

        return scaled


        



m = Matrix(4, 1, 2, 3)

print(m.aigenval())
print(m.aigenvecs())
print(m.scaledaigenvecs())
