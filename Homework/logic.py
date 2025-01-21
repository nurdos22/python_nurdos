import random


def game_settings(config):
    range_start = config("range_start")
    range_end = config("range_end")
    start_capital = config("start_capital")
    return range_start, range_end, start_capital


def play_game(range_start, range_end, start_capital):

    target_number = random.randint(range_start, range_end)
    print(f"Угадайте число от {range_start} до {range_end} , начальный капитал: {start_capital}")

    while True:
            bet = int(input("Введите вашу ставку: "))
            if bet > start_capital:
                print("Ставка превышает ваш капитал")
                continue

            guess = int(input(f"Введите число ({range_start}-{range_end}): "))

            if guess == target_number:
                print("Вы угадали")
                start_capital += bet
                print(f"Ваш капитал удвоился: {start_capital}")
                break
            else:
                print("Вы теряете ставку")
                start_capital -= bet
                if start_capital <= 0:
                    print("Игра окончена")
                    break

            print(f"Оставшийся капитал: {start_capital}")

    print(f"Вы не угадали. Загаданное число было: {target_number}")
