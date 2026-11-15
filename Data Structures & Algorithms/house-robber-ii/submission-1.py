class Solution:
    def rob(self, nums: List[int]) -> int:

        def canrob(nums, start, end):

            if start == end:
                return nums[start]

            dp = [0] * (len(nums))

            dp[start] = nums[start]
            dp[start+1] = max(nums[start], nums[start+1])

            for i in range(start+2, end+1):
                pick = dp[i-2] + nums[i]
                skip = dp[i-1]

                dp[i] = max(pick,skip)

            return dp[end]


        n = len(nums)

        if n == 1:
            return nums[0]

        n1 = canrob(nums,0, n-2)

        n2 = canrob(nums,1, n-1)


        return max(n1, n2)



        
        