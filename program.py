from program_base import ProgramBase
from argument_processor_base import ArgumentProcessorBase


class Program(ProgramBase):
    def __init__(self, argument_processor: ArgumentProcessorBase) -> None:
        self.argument_processor = argument_processor

    def start(self, argv: list[str]) -> None:
        self.argument_processor.process(argv)
