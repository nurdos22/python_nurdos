
import configparser
from logic import game_settings, play_game

def main():

    config = configparser.ConfigParser()
    config.read("settings.ini")


    def get_setting(setting_name):
        return int(config["Game_GUESS"][setting_name])


    range_start, range_end, start_capital = game_settings(get_setting)


    play_game(range_start, range_end, start_capital)

if __name__ == "__main__":
    main()
