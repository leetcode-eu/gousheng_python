
import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = collections.Counter(s)
        ans = ""
        for c in sorted(hash_map, key = lambda item: hash_map[item], reverse = True):
            ans += c * hash_map[c]

        return ans
