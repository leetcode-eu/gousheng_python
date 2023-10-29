
import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        length_of_string = len(s)
        hash_dict = collections.defaultdict(int)  # key: letter ; value: maximum position of certain letter
        left_pointer, right_pointer = 0, -1
        max_length = 0

        while right_pointer + 1 <= length_of_string - 1:

            # 1.
            right_pointer += 1
            hash_dict[s[right_pointer]] = right_pointer

            # 2.
            if len(hash_dict) == k + 1:
                minimum_position = min(hash_dict.values())

                for letter, position in hash_dict.items():
                    if position == minimum_position:
                        minimum_position_letter = letter

                del hash_dict[minimum_position_letter]
                left_pointer = minimum_position + 1

            # 3.
            max_length = max(max_length, right_pointer - left_pointer + 1)

        return max_length