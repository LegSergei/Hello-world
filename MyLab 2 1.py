string = (input("Введите строку\n"))
alpf = "абвгдежзийклмнопрстуфхчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФЧСШЩЪЫЬЭЮЯ"
local_string = ""  #В этой переменной слово собирается по символам
new_string = ""  #В этой переменной хранятся все слова, удовлетворяющие условию
n = None # Счетчик состояния. Если n = 1, значит первая буква Л, если n = 2, первая буква Л, а вторая и
for symb in string:

    if symb in alpf:  # Если символ принадлежит строке alpf, значит это буква
        if n == 1 and symb != "и":
            n = None
            local_string = ""

        if n == 2:
            local_string += symb

        if symb == "Л":
            local_string += symb
            n = 1

        if symb == "и" and n == 1:
            local_string += symb
            n = 2

    else:
        if n == 2:
            new_string += local_string + " "
        local_string = ""
        n = None


new_string += local_string + " "
print(new_string)
