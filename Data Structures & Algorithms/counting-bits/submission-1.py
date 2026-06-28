class Solution:
    def countBits(self, n: int) -> List[int]:


        arr = []

        def counter(x):
            count = 0

            while x>0:
                count += x%2
                x //= 2

            return count

        for i in range(n+1):
            k = counter(i)
            arr.append(k)

        return arr





        

        