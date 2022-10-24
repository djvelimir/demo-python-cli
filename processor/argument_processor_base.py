from abc import ABC, abstractmethod


class ArgumentProcessorBase(ABC):
    @abstractmethod
    def process(self, args: list[str]) -> None:
        pass
