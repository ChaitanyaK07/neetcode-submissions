
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)

        left = 1
        right = max(piles)
        ans = min(piles)

        while left <= right:
            mid = left + (right - left)//2
            tot = 0


            for i in range(n):
                tot += math.ceil(piles[i]/mid)

            if tot <= h:
                ans = mid
                right = mid-1
            else:
                left = mid+1


        return ans




        