from fractions import Fraction
import math

pi = 3.14159265359

class vec2:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x * other.x, self.y * other.y)
        return vec2(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, vec2):
            return vec2(
                self.x / (other.x if other.x != 0 else 1e-8),
                self.y / (other.y if other.y != 0 else 1e-8)
            )
        return vec2(
            self.x / (other if other != 0 else 1e-8),
            self.y / (other if other != 0 else 1e-8)
        )

    def __neg__(self):
        return vec2(-self.x, -self.y)

    def __repr__(self):
        return f"vec2({self.x}, {self.y})"

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        l = self.length()
        if l == 0:
            return vec2(0, 0)
        return self / l

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    @staticmethod
    def cross_scalar_vec(s, v):
        return vec2(-s * v.y, s * v.x)

    @staticmethod
    def cross_vec_scalar(v, s):
        return vec2(s * v.y, -s * v.x)
    
def decimal_to_fraction(decimal_str):
    return Fraction(decimal_str).limit_denominator()

def smart_number(decimal_str):
    frac = Fraction(decimal_str).limit_denominator()
    dec = str(float(decimal_str))
    
    if len(str(frac)) < len(dec):
        return frac
    else:
        return dec