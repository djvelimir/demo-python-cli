from src.processor.argument_processor_base import ArgumentProcessorBase
from src.program.program_base import ProgramBase


class Program(ProgramBase):
    __argument_processor: ArgumentProcessorBase

    def __init__(self, argument_processor: ArgumentProcessorBase) -> None:
        self.__argument_processor = argument_processor

    def start(self, args: list[str]) -> None:
        self.__argument_processor.process(args)
