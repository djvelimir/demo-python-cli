from generator.random_character_generator import RandomCharacterGeneratorBase
from shuffler.string_shuffler_base import StringShufflerBase
from src.generator.password_generator_base import PasswordGeneratorBase


class PasswordGenerator(PasswordGeneratorBase):
    __password_length: int
    __random_character_generator: RandomCharacterGeneratorBase = None
    __string_shuffler: StringShufflerBase = None

    def __init__(self,
                 random_character_generator: RandomCharacterGeneratorBase,
                 string_shuffler: StringShufflerBase) -> None:
        self.__password_length = 16
        self.__random_character_generator = random_character_generator
        self.__string_shuffler = string_shuffler

    def generate(self) -> str:
        password: str = ''
        password = password + self.__random_character_generator.generate_uppercase_character()
        password = password + self.__random_character_generator.generate_lowercase_character()
        password = password + self.__random_character_generator.generate_digit_character()
        password = password + self.__random_character_generator.generate_special_character()

        for i in range(0, self.__password_length - 4):
            password = password + self.__random_character_generator.generate_allowed_character()

        return self.__string_shuffler.shuffle(password)
