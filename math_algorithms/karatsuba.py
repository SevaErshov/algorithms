#O(n^(log(3)))
#Числа равны по числу разрядов и являются степенью двойки

def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    length = len(str(x))
    half = length // 2
    a, b = x // (10 ** half), x % (10 ** half)
    c, d = y // (10 ** half), y % (10 ** half)

    abcd = karatsuba((a + b), (c + d))
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    return  ac * (10 ** length) + (abcd - ac - bd) * (10 ** half) + bd

