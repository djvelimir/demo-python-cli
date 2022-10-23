from abc import ABC, abstractmethod


class PasswordGeneratorBase(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass
