
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        length_of_string           = len(s)
        hash_dict                  = defaultdict(int)  # key: letter ; value: maximum position of certain letter
        left_pointer ,right_pointer = 0, -1
        max_length                 = 0

        while right_pointer +1 <= length_of_string -1:

            # 1.
            right_pointer               += 1
            hash_dict[s[right_pointer]]  = right_pointer

            # 2.
            if len(hash_dict) == 3:
                minimum_position = min(hash_dict.values())

                for letter, position in hash_dict.items():
                    if position == minimum_position:
                        minimum_position_letter = letter

                left_pointer = minimum_position + 1
                del hash_dict[minimum_position_letter]

            # 3.
            max_length = max(max_length, right_pointer - left_pointer + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    sol.lengthOfLongestSubstringTwoDistinct("eceba")