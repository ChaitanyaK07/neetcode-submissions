class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        pr = 1
        n = len(nums)
        out = [0] * (n)

        for i in range(n):
            left = 1
            right = 1
            for j in range(0, i):
                left *= nums[j]
            for k in range(i+1, n):
                right *= nums[k]
            
            out[i] = left*right

        return out
        