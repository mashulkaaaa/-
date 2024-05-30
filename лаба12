# Метод половинного деления

def F(x):
    return x**4 - 3*x**2 + 4*x - 5.9

a = float(input("Введите a: "))
b = float(input("Введите b: "))
eps = float(input("Введите Eps: "))

while abs(b - a) > eps:
    x = (a + b) / 2
    if (F(x) == 0): break
    if (F(a) * F(x) > 0):
        a = x
    else:
        b = x

print('x =',x)
print('F(x) = ', F(x))
