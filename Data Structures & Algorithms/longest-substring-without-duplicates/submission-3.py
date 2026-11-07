class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        first = 0

        max_len = 0
        freq_map = {}

        for sec in range(first,n):

            freq_map[s[sec]] = freq_map.get(s[sec], 0) + 1

            while freq_map[s[sec]] > 1:
                freq_map[s[first]] -= 1
                first += 1

            max_len = max(max_len, sec - first + 1)


        return max_len


            

        


         
        