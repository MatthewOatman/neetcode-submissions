class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        what my head initially goes to is using a hash set or fixed array of size 9 with each of the numbers refering to the index num - 1 and that being to keep track of if the number is in there or not or if there is a rpeating. So essentially, each index is refering to a specfic count and you can construct a 2d list to represent the whole grid of the sodoku board. 

        Treat the outer array as the rows and each of the inner arrays as row with the different columns

        To check a valid row what we can do is go through each of the subarrays and ensure that each of the rows does not contain any values at indexes of more than 2

        To check a valid column we can iterate through each of the first indices holding the second index contstant and perform that check again. This makes me think that maybe constructing the whole new board again is not the smartest decision and insteaed we can have a hashmap for each of the checks
        '''

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # Where key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True






