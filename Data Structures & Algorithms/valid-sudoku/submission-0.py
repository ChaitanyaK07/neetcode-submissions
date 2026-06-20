class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                idx = (i//3) * 3 + (j//3)

                if val == ".":
                    continue

                if val in rows[i]:
                    return False

                if val in cols[j]:
                    return False

                if val in boxs[idx]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxs[idx].add(val)

        return True


        