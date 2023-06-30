   
class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        

    def count_words(self):
        words = self.sentence.split()
        self.word_count = len(words)

    def get_word_count(self):
        return self.word_count

    def get_shortest_word(self):
        words = self.sentence.split()
        shortest_word_length = min(len(word) for word in words)
        return shortest_word_length

    def get_longest_word(self):
        words = self.sentence.split()
        longest_word_length = max(len(word) for word in words)
        return longest_word_length




