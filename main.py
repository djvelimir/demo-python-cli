import sys
from validator.argument_validator_base import ArgumentValidatorBase
from validator.argument_validator import ArgumentValidator
from generator.password_generator_base import PasswordGeneratorBase
from generator.password_generator import PasswordGenerator
from display.terminal_base import TerminalBase
from display.terminal import Terminal
from processor.argument_processor_base import ArgumentProcessorBase
from processor.argument_processor import ArgumentProcessor
from program.program_base import ProgramBase
from program.program import Program


def main(argv: list[str]) -> None:
    argument_validator: ArgumentValidatorBase = ArgumentValidator()
    password_generator: PasswordGeneratorBase = PasswordGenerator()
    terminal: TerminalBase = Terminal()
    argument_processor: ArgumentProcessorBase = ArgumentProcessor(argument_validator, password_generator, terminal)

    program: ProgramBase = Program(argument_processor)
    program.start(argv)


if __name__ == '__main__':
    main(sys.argv)
