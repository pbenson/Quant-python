class Complex(object):
    def __init__(self, real, imaginary):
        self.real  = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self. imaginary * no.imaginary
        imag = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imag)

    def __truediv__(self, no):
        return self * no.conjugate().scale(1 / no.abs2())

    def abs2(self):
        return self.real * self.real + self.imaginary * self.imaginary

    def conjugate(self):
        return Complex(self.real, -self.imaginary)

    def mod(self):
        return math.sqrt(abs2())

    def scale(self, scalar):
        return Complex(self.real * scalar, self.imaginary * scalar)

    def __repr__(self):
        return str(self.real) + '+' +str(self.imaginary)+'i'

z = Complex(3, 4)
w = Complex(3, 4)
print(z / w)