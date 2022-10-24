from program.program_base import ProgramBase
from processor.argument_processor_base import ArgumentProcessorBase


class Program(ProgramBase):
    __argument_processor: ArgumentProcessorBase

    def __init__(self, argument_processor: ArgumentProcessorBase) -> None:
        self.__argument_processor = argument_processor

    def start(self, argv: list[str]) -> None:
        self.__argument_processor.process(argv)
