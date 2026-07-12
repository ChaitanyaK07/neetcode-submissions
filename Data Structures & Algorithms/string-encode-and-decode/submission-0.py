class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for string in strs:
            result += str(len(string)) + "#" + string

        return result


    def decode(self, s: str) -> List[str]:

        result = []
        i = 0


        while i < len(s):

            j = i

            while s[j] != "#":
                j +=1

            leng = int(s[i:j])

            word_start = j+1

            word_end = word_start + leng


            word = s[word_start : word_end]

            result.append(word)

            i = word_end


        return result




