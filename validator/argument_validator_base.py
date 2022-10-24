from abc import ABC, abstractmethod


class ArgumentValidatorBase(ABC):
    @abstractmethod
    def validate(self, argv: list[str]) -> bool:
        pass
