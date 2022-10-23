from argument_processor_base import ArgumentProcessorBase
from argument_validator_base import ArgumentValidatorBase
from password_generator_base import PasswordGeneratorBase
from terminal_base import TerminalBase


class ArgumentProcessor(ArgumentProcessorBase):
    def __init__(self,
                 argument_validator: ArgumentValidatorBase,
                 password_generator: PasswordGeneratorBase,
                 terminal: TerminalBase) -> None:
        self.argument_validator = argument_validator
        self.password_generator = password_generator
        self.terminal = terminal

    def process(self, argv: list[str]) -> None:
        if self.argument_validator.validate(argv):
            password = self.password_generator.generate()
            self.terminal.show(password)
        else:
            self.terminal.show('Usage:\npython ./main.py generate password')
