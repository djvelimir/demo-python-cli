import random
from generator.password_generator_base import PasswordGeneratorBase


class PasswordGenerator(PasswordGeneratorBase):
    __PASSWORD_LENGTH: int = 16
    __UPPERCASE_CHARACTERS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __LOWERCASE_CHARACTERS: str = "abcdefghijklmnopqrstuvwxyz"
    __DIGIT_CHARACTERS: str = "0123456789"
    __SPECIAL_CHARACTERS: str = "~`!@#$%^&*()-_=+[{]}\\|;:\'\",<.>/?"
    __UNION_OF_ALLOWED_CHARACTERS: str =\
        __UPPERCASE_CHARACTERS +\
        __LOWERCASE_CHARACTERS +\
        __DIGIT_CHARACTERS +\
        __SPECIAL_CHARACTERS

    def generate(self) -> str:
        password: str = ''

        # generate at least one uppercase character
        password = password + self.__generate_random_character(self.__UPPERCASE_CHARACTERS)

        # generate at least one lowercase character
        password = password + self.__generate_random_character(self.__LOWERCASE_CHARACTERS)

        # generate at least one digit character
        password = password + self.__generate_random_character(self.__DIGIT_CHARACTERS)

        # generate at least one special character
        password = password + self.__generate_random_character(self.__SPECIAL_CHARACTERS)

        for i in range(4, self.__PASSWORD_LENGTH):
            # generate random character from union of allowed characters
            password = password + self.__generate_random_character(self.__UNION_OF_ALLOWED_CHARACTERS)

        # shuffle generated characters
        password = ''.join(random.sample(password, len(password)))

        return password

    @staticmethod
    def __generate_random_character(characters: str) -> str:
        return characters[random.randint(0, len(characters) - 1)]
