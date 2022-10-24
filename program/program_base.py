from abc import ABC, abstractmethod


class ProgramBase(ABC):

    @abstractmethod
    def start(self, argv: list[str]) -> None:
        pass
