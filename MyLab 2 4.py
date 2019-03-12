N = int(input("Введите количество элементов\n"))
while N <= 10:
    print("Количество элементов должно быть больше десяти")
    N = int(input("Введите количество элементов\n"))

list = [None] * N

for i in range (0, N):
    b = int(input("Введите " + str(i+1) + "-й " + "элемент\n"))
    list[i] = b
print("В списке " + str(len(list)) + " элементов")
for j in range (0 , N) [::-1]:
    if list[j]%2 == 0:
        del list[j]

for k in range (0,2):
    a = int(input("Введите дополнительный элемент №" + str(k+1) + "\n"))
    list.append(a)
print(list)