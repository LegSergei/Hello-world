a = float(input("a ="))
while a == 0:
    print("Деление на ноль! Введите a не равное нулю")
    a = float(input("a ="))
b = float(input("b ="))
while b == 0:
    print("Деление на ноль! Введите b не равное нулю")
    b = float(input("b ="))
c = float(input("c ="))
d = float(input("d ="))
k = float(input("k ="))
n = abs(((a**2 - b**3 - c**3 * a**2)*(b - c + c*(k - d/(b**3))) - (k/b - k/a)*c)**2 - 20000)
print (n)