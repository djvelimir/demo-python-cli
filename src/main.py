import sys

from display.terminal import Terminal
from display.terminal_base import TerminalBase
from generator.password_generator import PasswordGenerator
from generator.password_generator_base import PasswordGeneratorBase
from generator.random_character_generator import RandomCharacterGenerator
from generator.random_character_generator_base import RandomCharacterGeneratorBase
from processor.argument_processor import ArgumentProcessor
from processor.argument_processor_base import ArgumentProcessorBase
from program.program import Program
from program.program_base import ProgramBase
from shuffler.string_shuffler import StringShuffler
from shuffler.string_shuffler_base import StringShufflerBase
from validator.argument_validator import ArgumentValidator
from validator.argument_validator_base import ArgumentValidatorBase


def main(args: list[str]) -> None:
    argument_validator: ArgumentValidatorBase = ArgumentValidator()
    string_shuffler: StringShufflerBase = StringShuffler()
    random_character_generator: RandomCharacterGeneratorBase = RandomCharacterGenerator()
    password_generator: PasswordGeneratorBase = PasswordGenerator(random_character_generator, string_shuffler)
    terminal: TerminalBase = Terminal()
    argument_processor: ArgumentProcessorBase = ArgumentProcessor(argument_validator, password_generator, terminal)

    program: ProgramBase = Program(argument_processor)
    program.start(args)


if __name__ == '__main__':
    main(sys.argv)
