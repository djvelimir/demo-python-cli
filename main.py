import sys
from argument_validator_base import ArgumentValidatorBase
from argument_validator import ArgumentValidator
from password_generator_base import PasswordGeneratorBase
from password_generator import PasswordGenerator
from terminal_base import TerminalBase
from terminal import Terminal
from argument_processor_base import ArgumentProcessorBase
from argument_processor import ArgumentProcessor
from program_base import ProgramBase
from program import Program


def main(argv: list[str]) -> None:
    argument_validator: ArgumentValidatorBase = ArgumentValidator()
    password_generator: PasswordGeneratorBase = PasswordGenerator()
    terminal: TerminalBase = Terminal()
    argument_processor: ArgumentProcessorBase = ArgumentProcessor(argument_validator, password_generator, terminal)

    program: ProgramBase = Program(argument_processor)
    program.start(argv)


if __name__ == '__main__':
    main(sys.argv)
