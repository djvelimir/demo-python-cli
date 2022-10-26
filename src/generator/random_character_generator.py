import random

from generator.random_character_generator_base import RandomCharacterGeneratorBase


class RandomCharacterGenerator(RandomCharacterGeneratorBase):
    __uppercase_characters: str = None
    __lowercase_characters: str = None
    __digit_characters: str = None
    __special_characters: str = None
    __allowed_characters: str = None

    def __init__(self) -> None:
        self.__uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__lowercase_characters = "abcdefghijklmnopqrstuvwxyz"
        self.__digit_characters = "0123456789"
        self.__special_characters = "~`!@#$%^&*()-_=+[{]}\\|;:\'\",<.>/?"
        self.__allowed_characters = \
            self.__uppercase_characters + \
            self.__lowercase_characters + \
            self.__digit_characters + \
            self.__special_characters

    def generate_uppercase_character(self) -> str:
        return self.__uppercase_characters[random.randint(0, len(self.__uppercase_characters) - 1)]

    def generate_lowercase_character(self) -> str:
        return self.__lowercase_characters[random.randint(0, len(self.__lowercase_characters) - 1)]

    def generate_digit_character(self) -> str:
        return self.__digit_characters[random.randint(0, len(self.__digit_characters) - 1)]

    def generate_special_character(self) -> str:
        return self.__special_characters[random.randint(0, len(self.__special_characters) - 1)]

    def generate_allowed_character(self) -> str:
        return self.__allowed_characters[random.randint(0, len(self.__allowed_characters) - 1)]
