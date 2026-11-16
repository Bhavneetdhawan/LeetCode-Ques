class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Store existing numbers and identify empty cells
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == '.':
                    empty.append((r, c))
                else:
                    box = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def backtrack(pos):
            if pos == len(empty):
                return True

            # Select the empty cell with the fewest possible choices
            best = pos
            best_options = None

            for i in range(pos, len(empty)):
                r, c = empty[i]
                box = (r // 3) * 3 + (c // 3)

                options = set("123456789") - rows[r] - cols[c] - boxes[box]

                if not options:
                    return False

                if best_options is None or len(options) < len(best_options):
                    best = i
                    best_options = options

                if len(options) == 1:
                    break

            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            box = (r // 3) * 3 + (c // 3)

            for num in best_options:
                board[r][c] = num

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if backtrack(pos + 1):
                    return True

                # Undo the choice if it leads to an invalid solution
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)
                board[r][c] = '.'

            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        backtrack(0)