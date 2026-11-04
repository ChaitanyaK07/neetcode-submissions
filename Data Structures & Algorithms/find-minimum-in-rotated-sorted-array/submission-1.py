class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()

        left = 0
        right = n-1
        ans = nums[0]

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid+1]:
                ans = min(ans,nums[mid])
                left = mid + 1

            else:
                right = mid - 1


        return ans


        