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

        if a != 0 or b != 0:
            return (b, -a)

        if c != 0 or d != 0:
            return (d, -c)

        return (0, 0)

    def aigenvecs(self):
        return [(v, self.aigenvec(v)) for v in self.aigenval()]
    
    def checkfor0vec(self, vec: tuple) -> bool:
        if vec[0] == 0 and vec[1] == 0:
            return True
    
    def scaledaigenvecs(self):
        vals = [self.aigenvec(v) for v in self.aigenval()]
        scaled = []
        counter = 0
        for vec in vals:
            counter += 1
            
            if self.checkfor0vec(vec):
                scaled.append("UNDEFINED MATRIX")
            else:
                scale = math.gcd(int(vec[0]), int(vec[1]))
                if scale == 0:
                    scaled.append(vec)

                else:
                    scaled.append(tuple(x / scale for x in vec))

        return scaled



        



a = Matrix(0, 0, 0, 0)
b = Matrix(1, 0, 1, 0)
c = Matrix(0, 1, 0, 1)
eigenvalues_a = a.aigenval()
eigenvalues_b = b.aigenval()
eigenvalues_c = c.aigenval()
eigenvecs_a = a.scaledaigenvecs()
eigenvecs_b = b.scaledaigenvecs()
eigenvecs_c = c.scaledaigenvecs()

print("-----------------------------")
for i in range (len(eigenvalues_a)):
    print(f"Eigenvalue a: {eigenvalues_a[i]}")
print("-----------------------------")
for i in range(len(eigenvecs_a)):
    print(f"Eigenvector a: {eigenvecs_a[i]}")
print("-----------------------------")
for i in range(len(eigenvalues_b)):
    print(f"Eigenvalue b: {eigenvalues_b[i]}")
print("-----------------------------")
for i in range(len(eigenvecs_b)):
    print(f"Eigenvector b: {eigenvecs_b[i]}")
print("-----------------------------")
for i in range(len(eigenvalues_c)):
    print(f"Eigenvalue c: {eigenvalues_c[i]}")
print("-----------------------------")
for i in range(len(eigenvecs_c)):
    print(f"Eigenvector c: {eigenvecs_c[i]}")
print("-----------------------------")