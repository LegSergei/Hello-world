my_string = "ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;" \
            "_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;" \
            "22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;" \
            "_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;" \
            "21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;" \
            "_Петров Всеволод Борисович;21 год;Студент 2 курса"
spisok = my_string.split(";_")
for i in range(0, len(spisok)):
    if i == 0:
        new_string = spisok[i]
        new_string = new_string.split(";")
        print("\t\t", " " + new_string[0] + " "*19 + new_string[1] + " "*14 + new_string[2])
    else:
        new_string = spisok[i]
        if "21" in new_string:
            new_string = new_string.split(";")
            print(new_string[0].ljust(32) + new_string[1].ljust(7) + " " * 12 + new_string[2])