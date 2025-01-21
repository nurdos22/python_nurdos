
import configparser
from logic import game_settings, play_game

def main():
    # Считываем настройки из settings.ini
    config = configparser.ConfigParser()
    config.read("settings.ini")

    # Функция для получения значений настроек
    def get_setting(setting_name):
        return int(config["Game_GUESS"][setting_name])

    # Получаем параметры игры
    range_start, range_end, start_capital = game_settings(get_setting)

    # Запускаем игру
    play_game(range_start, range_end, start_capital)

if __name__ == "__main__":
    main()
