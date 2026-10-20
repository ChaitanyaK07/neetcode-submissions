class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dup = set()

        for i in nums:
            dup.add(i)

        if len(dup) == len(nums):
            return False

        return True


        