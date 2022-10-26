from abc import ABC, abstractmethod


class RandomCharacterGeneratorBase(ABC):
    @abstractmethod
    def generate_uppercase_character(self) -> str:
        pass

    @abstractmethod
    def generate_lowercase_character(self) -> str:
        pass

    @abstractmethod
    def generate_digit_character(self) -> str:
        pass

    @abstractmethod
    def generate_special_character(self) -> str:
        pass

    @abstractmethod
    def generate_allowed_character(self) -> str:
        pass
