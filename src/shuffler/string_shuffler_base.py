from abc import ABC, abstractmethod


class StringShufflerBase(ABC):
    @abstractmethod
    def shuffle(self, characters: str) -> str:
        pass
