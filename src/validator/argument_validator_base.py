from abc import ABC, abstractmethod


class ArgumentValidatorBase(ABC):
    @abstractmethod
    def validate(self, args: list[str]) -> bool:
        pass
