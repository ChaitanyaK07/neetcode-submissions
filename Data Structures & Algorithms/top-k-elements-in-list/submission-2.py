class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freqmap = {}


        for num in nums:
            freqmap[num] = freqmap.get(num, 0) + 1

        res = []

        for i in range(k):
            l = max(freqmap, key = freqmap.get)
            res.append(l)
            del freqmap[l]

        return res


        