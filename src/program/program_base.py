from abc import ABC, abstractmethod


class ProgramBase(ABC):

    @abstractmethod
    def start(self, args: list[str]) -> None:
        pass
