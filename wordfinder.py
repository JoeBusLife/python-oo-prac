"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, word_file):
        self.word_list = self.create_word_list(word_file)
        print(f'{len(self.word_list)} words read')
        
    def create_word_list(self, word_file):
        with open(word_file, "r") as file:
            return [line.strip() for line in file]
        
    def random(self):
        return choice(self.word_list)
    
class SpecialWordFinder(WordFinder):
    """Version of Word Finder that ignores lines not containing dictionary words"""
    def create_word_list(self, word_file):
        with open(word_file, "r") as file:
            return [line.strip() for line in file if line.strip() != "" and line[0] != "#"]