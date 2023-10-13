
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)
        word_length = len(beginWord)
        deque = [(beginWord, 1)]

        while deque:
            word, step = deque.pop(0)
            if word == endWord:
                return step

            for i in range(word_length):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + letter + word[i + 1:]
                    if new_word in word_set:
                        deque.append((new_word, step + 1))
                        word_set.remove(new_word)

        return 0