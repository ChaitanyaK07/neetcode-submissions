class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        first = 0

        seen = {}
        max_len = 0

        for sec in range(len(s)):

            char = s[sec]

            if char in seen and seen[char] >= first:
                first = seen[char] + 1
                

            seen[char] = sec

            max_len = max(max_len, sec - first + 1)


        return max_len


         
        