import decimal


class Triangle:
    def type(self, a, b, c):
        if a < 0:
            return "a can't be 0"
        if b < 0:
            return "b can't be 0"
        if c < 0:
            return "c can't be 0"
        if a >= 800:
            return "a is not in the value range"
        if b >= 800:
            return "b is not in the value range"
        if c >= 800:
            return "c is not in the value range"
        if a + c > b and a + b > c and c + b > a:
            if a == b == c:
                return "Equilateral triangle"
            elif a == b or b == c or b == c:
                return "Isosceles triangle"
            else:
                return "Common triangle"
        else:
            return "Not triangle"


def compute(a, b, c):
    t = Triangle().type(a, b, c)  # 实例化收费系统

    return t


if __name__ == '__main__':
    compute()
