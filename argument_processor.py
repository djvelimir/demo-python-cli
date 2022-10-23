from argument_processor_base import ArgumentProcessorBase
from argument_validator_base import ArgumentValidatorBase
from password_generator_base import PasswordGeneratorBase
from terminal_base import TerminalBase


class ArgumentProcessor(ArgumentProcessorBase):
    __argument_validator: ArgumentValidatorBase = None
    __password_generator: PasswordGeneratorBase = None
    __terminal: TerminalBase = None

    def __init__(self,
                 argument_validator: ArgumentValidatorBase,
                 password_generator: PasswordGeneratorBase,
                 terminal: TerminalBase) -> None:
        self.__argument_validator = argument_validator
        self.__password_generator = password_generator
        self.__terminal = terminal

    def process(self, argv: list[str]) -> None:
        if self.__argument_validator.validate(argv):
            password = self.__password_generator.generate()
            self.__terminal.show(password)
        else:
            self.__terminal.show('Usage:\npython ./main.py generate password')
