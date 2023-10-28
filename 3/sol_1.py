

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length_of_string = len(s)
        unique_letters_set = set()
        right_pointer = -1
        max_length = 0

        for i in range(length_of_string):

            if i != 0:
                unique_letters_set.remove(s[i - 1])

            while right_pointer + 1 <= length_of_string - 1 and s[right_pointer + 1] not in unique_letters_set:
                right_pointer += 1
                unique_letters_set.add(s[right_pointer])

            max_length = max(max_length, right_pointer - i + 1)

        return max_length