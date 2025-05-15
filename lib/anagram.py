# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        result = []
        original = sorted(self.word.lower())

        for word in word_list:
            if sorted(word.lower()) == original:
                result.append(word)
        return result