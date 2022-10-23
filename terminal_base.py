from abc import ABC, abstractmethod


class TerminalBase(ABC):
    @abstractmethod
    def show(self, message: str) -> None:
        pass
