class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for index,i in enumerate(sentence):
            if i.startswith(searchWord):return index+1
        return -1
        