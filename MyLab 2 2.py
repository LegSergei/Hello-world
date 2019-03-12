my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
spisok = my_string.split(";_")
for i in range(0, len(spisok)):
    if i == 0:
        new_string = spisok[i]
        new_string = new_string.split(";")
        print("\t\t", " " + new_string[0] + new_string[1] + new_string[2] + " " * 17 + new_string[3] + " " * 14 + new_string[4])
    else:
        new_string = spisok[i]
        new_string = new_string.split(";")
        first_string = new_string[0] + " " + new_string[1] + " " + new_string[2]
        print(first_string.ljust(30) + new_string[3].ljust(7) + " "*12 + new_string[4])
