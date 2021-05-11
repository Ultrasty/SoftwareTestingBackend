import decimal

class Triangle:
   def type(self, a, b, c):
        if a<0:
            return "a不能为0"
        if b<0:
            return "b不能为0"
        if c<0:
            return "c不能为0"
        if a>=800:
            return "a不在取值范围内"
        if b>=800:
            return "b不在取值范围内"
        if c>=800:
            return "c不在取值范围内"
        if a+c > b and a+b > c and c+b > a:
            if a == b == c:
                return "等边三角形"
            elif a == b or b == c or b == c:
                return "等腰三角形"
            else:
                return "普通三角形"
        else:
            return "不是三角形"


def main():
    record=input("请输入a,b,c（用\",\"分隔）:")
    try:
        
        a=float(record.split(",")[0])
        b=float(record.split(",")[1])
        c=float(record.split(",")[2])
    except IndexError:
        print("请输入足够的值")
        return
    except ValueError:
        print("a,b,c需要为常数")
        return
    
    t = Triangle().type(a,b,c)  # 实例化收费系统

    print(t)


if __name__ == '__main__':
    main()