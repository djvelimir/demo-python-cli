from dependency_injector import containers, providers

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


class Container(containers.DeclarativeContainer):
    argument_validator: ArgumentValidatorBase = providers.Factory(
        ArgumentValidator
    )

    string_shuffler: StringShufflerBase = providers.Factory(
        StringShuffler
    )

    random_character_generator: RandomCharacterGeneratorBase = providers.Factory(
        RandomCharacterGenerator
    )

    password_generator: PasswordGeneratorBase = providers.Factory(
        PasswordGenerator,
        random_character_generator=random_character_generator,
        string_shuffler=string_shuffler
    )

    terminal: TerminalBase = providers.Factory(
        Terminal
    )

    argument_processor: ArgumentProcessorBase = providers.Factory(
        ArgumentProcessor,
        argument_validator=argument_validator,
        password_generator=password_generator,
        terminal=terminal
    )

    program: ProgramBase = providers.Factory(
        Program,
        argument_processor=argument_processor
    )
