import random

from src.shuffler.string_shuffler_base import StringShufflerBase


class StringShuffler(StringShufflerBase):
    def shuffle(self, characters: str) -> str:
        return ''.join(random.sample(characters, len(characters)))
