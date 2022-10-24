from abc import ABC, abstractmethod


class ArgumentProcessorBase(ABC):
    @abstractmethod
    def process(self, argv: list[str]) -> None:
        pass
