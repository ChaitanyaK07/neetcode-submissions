class Solution:
    def countBits(self, n: int) -> List[int]:


        array = [0] * (n+1)

        def counter(n):
            count = 0

            while n>0:
                count += n%2
                n = n // 2
            
            return count



        for i in range(n+1):
            k = counter(i)
            array[i] = k

        return array





        

        