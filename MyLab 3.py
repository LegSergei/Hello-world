import os.path
import sys

def main_menu():
    choise = "9"
    while choise != "0":
        print(
            """
            Меню выбора функций

            0 - Выход
            1 - Посчитать количество файлов в заданной директории
            2 - Сортировка списка товаров по цене
            3 - Уменьшить количество товаров
            """
        )
        choise = input("\n" + "Введите команду" + " ")
        while choise not in ["1", "2", "3", "0"]:
            choise = input("Команда не распознана. Введите '1', '2', '3' или '0'.\n")
        if choise == "1":
            chislo_failov()
            exit_or_continue()
        if choise == "2":
            sortirovka()
            save(gl_list)
            exit_or_continue()
        if choise == "3":
            decrease()
            save(gl_list)
            exit_or_continue()
        if choise == "0":
            sys.exit()


def chislo_failov():
    path = input("Введите директорию" + "\n")
    files = os.listdir(path)
    chislo = len(files)
    print("В указанной директории " + str(chislo) + " файла(ов)")


def sortirovka():
    global gl_list
    text_file = open("products.txt", "r")
    lines = text_file.readlines()
    for i in range(0, len(lines)):
        list = lines[i].strip()
        list = list.split(";")
        lines[i] = list
    new_list = sorted(lines, key=lambda j: j[2], reverse=True)
    for i in range(0, len(new_list)):
        print(new_list[i][0].ljust(3) + " " * 5 + new_list[i][1].ljust(20) \
              + " " * 5 + new_list[i][2].ljust(4) + " " * 5 + new_list[i][3].ljust(10))
    gl_list = new_list
    text_file.close()
    return gl_list


def exit_or_continue():
    reshenie = input("Вы хотите продолжить? ")
    while reshenie not in ["да", "yes", "Y", "1", "нет", "no", "N", "0"]:
        print("Ответ не распознан")
        reshenie = input("Вы хотите продолжить? ")
    if reshenie in ["да", "yes", "Y", "1"]:
        main_menu()
    elif reshenie in ["нет", "no", "N", "0"]:
        sys.exit()


def decrease():
    global gl_list
    text_file = open("products.txt", "r")
    lines = text_file.readlines()
    for i in range(0, len(lines)):
        list = lines[i].strip()
        list = list.split(";")
        lines[i] = list
    print(lines)
    a = input("Введите через запятую номера товаров, число которых нужно уменьшить\n")
    a = a.split(",")
    c = input("Введите число, на которое нужно уменьшить количество товаров. "
              "Если число превысит количество оставшегося товара, количество станет равно нулю.\n")
    for j in range(0, len(a)):
        n = int(a[j])
        k = int(lines[n][3])
        k = k - int(c)
        if k < 0:
            lines[n][3] = 0
        else:
            lines[n][3] = k
    print(lines)
    gl_list = lines
    text_file.close()
    return gl_list

def save(gl_list):
    save = "9"
    while save !="0":
        save = input("Желаете сохранить изменения файл? Y/N\n")
        while save not in ["Y", "N"]:
            save = input("Команда не распознана. Введите 'Y' или 'N'.\n")
        if save == "Y":
            print(
                """
Желаете сохранить изменения в новый файл?

1 - Сохранить в новый файл
2 - Сохранить в старый файл
                """)
            file = input()
            while file not in ["1", "2"]:
                file = input("Команда не распознана. Введите '1' или '2'.\n")
            if file == "1":
                name = input("Введите название файла")
                new_file = open(name+".txt", "w")
                for k in range(0, len(gl_list)):
                    for z in range(0, len(gl_list[k])):
                        s = str(gl_list[k][z])
                        if z == (len(gl_list) - 1):
                            new_file.write(s)
                        else:
                            new_file.write(s + ";")
                    new_file.write("\n")
                new_file.close()
            else:
                new_file = open("products.txt", "w")
                for k in range(0, len(gl_list)):
                    for z in range(0, len(gl_list[k])):
                        s = str(gl_list[k][z])
                        if z == (len(gl_list) - 1):
                            new_file.write(s)
                        else:
                            new_file.write(s + ";")
                    new_file.write("\n")
                new_file.close()

            save = "0"

        else:
            save = "0"


main_menu()
