import decimal


class Triangle:
    def type(self, a, b, c):
        if a == 0:
            return "a can't be 0"
        if b == 0:
            return "b can't be 0"
        if c == 0:
            return "c can't be 0"
        if a < 0:
            return "a can't < 0"
        if b < 0:
            return "b can't < 0"
        if c < 0:
            return "c can't < 0"
        if a >= 800:
            return "a is not in the range of value"
        if b >= 800:
            return "b is not in the range of value"
        if c >= 800:
            return "c is not in the range of value"
        if a + c > b and a + b > c and c + b > a:
            if a == b == c:
                return "Equilateral triangle"
            elif a == b or b == c or a == c:
                return "Isosceles triangle"
            else:
                return "Normal triangle"
        else:
            return "Not triangle"


def compute(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    t = Triangle().type(a, b, c)  # 实例化收费系统

    return t


