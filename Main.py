UNKNOWN_COM = "\nНеизвестная команда :("


# Текстовый декоратор(добавляет под строкой строку с "=" в зависимости от кол-ва символов декорируемой строки
def text_dec(text):
    print(text)
    printing = "=" * len(text)
    print(printing)


# Информация о игре
def about(inp):
    my_about = "<<Rand>>, версия 0.83(приватный некоммерческий проект)"
    # для отображения в главном меню
    if inp == "about":
        print("\n" + my_about)
        print("Дата компиляции: 11.02.2020")
        text_dec("Разработчик: @onstabb")
    # Для отображения в начале игры
    else:
        text_dec(my_about)
        text_dec(inp)
        # Описание игры
        print(
            "Суть игры в том, что нужно выбирать число от 1-го до 99-ти.\nИгра даёт первоначальный банк в размере 1000."
            "\nЕсли выбранное число больше чем число противника(компьютера) - выигрыш. "
            "\nВыигрыш получается по формуле 100 минус выбранное число. "
            "\nПри проигрыше отнимается так же по формуле.\nЧем меньше число, тем выше риск, но больше выигрыш.")

        # Декорирование последнего предложения(строки) описания игры
        text_dec("Чем выше число, риск меньше, но выигрыш небольшой.")
        print("Чтобы запустить игру введите что-нибудь")


# Отображение, проверка счета игрока, AI и вывод результата
def score(pl, ai, cash, w, lu, d, gc):
    msg = "\nВаш счет: {0}\nСчет противника: {1}".format(pl, ai)
    print(msg)
    if ai > pl:
        cash -= (100 - pl)
        lu += 1
        if cash < 0:
            cash = 0
        lose = "Проиграл! Текущий банк: " + str(cash)
        text_dec(lose)
    elif ai < pl:  # И здесь проверяется и обрабатывается параметр
        if opt1 is True:
            if pl < 85:
                cash += (100 - pl)
            else:
                cash += 0
        else:
            cash += (100 - pl)
        w += 1
        win = "Твоя взяла! Текущий банк: " + str(cash)
        text_dec(win)
    elif ai == pl:
        d += 1
        draw = "Ничья. Текущий банк: " + str(cash)
        text_dec(draw)
        # В любом исходе игры прибавляется соответствующая статистика
    gc += 1
    return cash, w, lu, d, gc


# Отображение статистики (эксп.функция)
def print_stats(w, lo, d, gc):
    print("=" * 15)
    print("Побед:", w)
    print("Поражений:", lo)
    print("Ничьи:", d)
    print("Всего игр:", gc)
    print("=" * 15)


# ИИ противника
def ai_beh(int_pl):
    import random
    int_ai = int_pl + random.randint(-80, 100)
    if int_ai > 100:
        int_ai = random.randint(int_pl, 100)
    elif int_ai < 1:
        int_ai = random.randint(0, int_pl)
    del random
    return int_ai


# Усложненный AI
def ai_hard_beh(int_pl):
    import random
    int_ai = int_pl + random.randint(-57, 115)
    if int_ai > 100:
        int_ai = random.randint(int_pl, 100)
    elif int_ai < 1:
        int_ai = random.randint(0, int_pl)
    del random
    return int_ai


# Экран от ввода строки в численном вводе
def shield_inp(put):
    while True:
        try:
            value = int(input(put))
            break
        except (ValueError, NameError):
            text_dec("\nВведи именно число!")
    return value


# Запись статистики на файл
def writefile():
    wr = open("save.txt", "r")
    f = wr.readlines()
    save_number = 0
    for line in f:
        if "Сейв №" in line:
            save_number = line.split(' ')[-1]
            save_number = int(save_number)
    if save_number >= 0:
        save_number += 1
    wr.close()
    wr = open("save.txt", "a")
    wr.write("Сейв №: {0}".format(save_number))
    wr.write("\nДеньги: {0}".format(money))
    wr.write("\nПобед: {0}\nПоражений: {1}\nНичьи: {2}\nВсего игр: {3}\n\n".format(stat_win,
                                                                                   stat_lose, stat_draw, all_games))
    wr.close()


# Считывание кол-ва денег (грубоватый метод)
def readfile():
    try:
        r_file = open("save.txt", "r")
        f = r_file.readlines()
        stat_money = 0
        for line in f:
            if "Деньги" in line:
                stat_money = line.split(' ')[-1]
                r_file.close()
                stat_money = int(stat_money)
        if stat_money != 0:
            return stat_money
        else:
            return 1000
    except FileNotFoundError:
        r_file = open("save.txt", "w")
        r_file.close()
        return 1000


# Опции игры
def options(opt):
    global restart_gm
    while restart_gm is True:
        print()
        text_dec("Настройки")
        print("Чтобы задать уровень сложности введи:\n\"1\" - легкий\n\"2\" - сложный. " +
              "При сложном уровне выигрыш дается при числе менее 85-ти" + "\nи сложнее выиграть")
        print("Чтобы вернуться в меню введи Back")
        print("Чтобы сделать полный рестарт игры введи Restart")
        print("Чтобы сохраниться введи Save")
        op_input = str(input("> "))
        op_input = op_input.lower()
        if op_input == "2":
            opt = True
            text_dec("Сложный режим: On")
        # Вверху и внизу, в зависимости от введенного вода задается вкл/откл параметра игры
        elif op_input == "1":
            opt = False
            text_dec("Лёгкий режим: On")
        elif op_input == "back":
            text_dec("\nВозвращаюсь")
            break  # Брейк для выхода из меню
        elif op_input == "restart":
            writefile()
            restart_gm = False  # Задает параметр для цикла всей игры False, чтобы игра рестартнулась
        elif op_input == "save":
            writefile()  # Сохраняет статистику по ранее прописанной функции
            print("Сохранение завершено")
        else:
            text_dec(UNKNOWN_COM)  # Экран от непрописанного вода
    return opt


# Стартовый текст при запуске программы
def start_text():
    start_game_text = "Добро пожаловать в игру!"
    about(start_game_text)


# Тело игры
def the_game(game_on: bool):
    global restart_gm
    while game_on is True:
        restart_gm = True  # Отвечает за полный рестарт игры

        while restart_gm is True:  # Начало всей игры, параметры внизу по дефолту(статистика и кэш)
            global stat_win, stat_lose, stat_draw, all_games, money
            stat_win = 0
            stat_lose = 0
            stat_draw = 0
            all_games = 0
            money = readfile()  # Считывает сейв
            global opt1
            opt1 = False  # Переменная опции с заданной вкл/выкл (Изначально False)
            print()  # Отступ для красоты
            text_dec("Начало новой игры...")

            while restart_gm is True:  # Главное меню
                print("Главное меню. Твой кэш: " + str(money))
                print("Options - для открытия параметров\nPlay - чтобы играть\nExit - выйти из игры"
                      "\nAbout - о программе и разработчике")
                pl_input = str(input("> "))  # ожидание ввода
                pl_input = pl_input.lower()  # понижаю ввод до нижнего регистра букв
                if pl_input == "options":
                    opt1 = options(opt1)

                elif pl_input == "about":
                    about(pl_input)

                elif pl_input == "play":  # Игра начинается. Денег должно быть больше 0
                    print("=" * 6)
                    while money > 0:
                        print("Введи \"100\" для статистики, \"0\" - для выхода в гл.меню")
                        pl_int = shield_inp("Введи число от 1 до 99: ")

                        while pl_int > 100 or pl_int < 0:
                            pl_int = shield_inp("Введи корректное число!: ")  # Цикл, если ввод числа неккоректный

                        # Тут определяется(внизу) включен ли параметр
                        if 0 < pl_int < 100:
                            if opt1 is True:
                                ai_int = ai_hard_beh(pl_int)
                            else:
                                ai_int = ai_beh(pl_int)

                            # Началась проверка чисел Игрока и AI
                            result = score(pl_int, ai_int, money, stat_win, stat_lose, stat_draw, all_games)
                            # Запись результатов из функции
                            money = result[0]
                            stat_win = result[1]
                            stat_lose = result[2]
                            stat_draw = result[3]
                            all_games = result[4]

                        elif pl_int == 100:  # Опция для отображения статистики
                            print()
                            print_stats(stat_win, stat_lose, stat_draw, all_games)
                            print()
                        elif pl_int == 0:
                            text_dec("\nВыход в меню")
                            break
                    # Если кончается банк - игра перезапускается с обнулением статистики
                    if money <= 0:
                        print("Ты банкрот!")
                        writefile()
                        restart_gm = False
                # Выход из игры
                elif pl_input == "exit":
                    writefile()
                    restart_gm = False
                    game_on = False
                # Еще один экран от непрописанного ввода
                else:
                    text_dec(UNKNOWN_COM)