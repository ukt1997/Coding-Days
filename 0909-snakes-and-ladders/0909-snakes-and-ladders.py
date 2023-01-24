class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # 2d board -> Linear Board [1,2,3,4, ... ,35,36].
        board.reverse()
        for i in range(1,len(board),2): board[i].reverse()
        linearBoard = [0] + list(chain(*board))

        # BFS -> curToken + [1...6]
        queue, seen, cnt = [1], set(), 0
        seen.add(1)
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                #print(cur,cnt)
                if cur == len(linearBoard) -1: return cnt

                for i in range(cur+1, min(cur+7,len(linearBoard))):
                    nxt = linearBoard[i] if linearBoard[i] != -1 else i

                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
            cnt += 1 # increment every Level
        return -1