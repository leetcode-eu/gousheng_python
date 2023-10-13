
import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        alphabet_distribution_map = collections.Counter(s)
        i = 0
        length = len(s)
        result = [None] * length

        for alphabet in sorted(alphabet_distribution_map, key=alphabet_distribution_map.get, reverse=True):
            if alphabet_distribution_map[alphabet] > length // 2 + length % 2:
                return ""

            for _ in range(alphabet_distribution_map[alphabet]):
                if i >= length:
                    i = 1

                result[i] = alphabet
                i += 2

        return "".join(result)