def solution(map):
    def createMaze(temap):
        temap[0][0] = "2"
        temap[len(temap)-1][len(temap[len(temap)-1])-1] = "X"
        return temap

    def valid(maze, moves):
        for x, pos in enumerate(maze[0]):
            if pos == "2":
                start = x

        i = start
        j = 0
        for move in moves:
            
            if move == "L":
                i -= 1

            elif move == "R":
                i += 1

            elif move == "U":
                j -= 1

            elif move == "D":
                j += 1

            if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
                return False
            # elif (maze[j][i] == 1):
                #return False
        return True


    def findEnd(maze, moves):
        global totalMoves

        for x, pos in enumerate(maze[0]):
            if pos == "2":
                start = x

        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1

            elif move == "R":
                i += 1

            elif move == "U":
                j -= 1

            elif move == "D":
                j += 1

        if maze[j][i] == "X":
            #print(len(moves))
            totalMoves = len(moves)
            return totalMoves + 1
        return False

    bestmoves = []
    for i, m in enumerate(map):
        for j, n in enumerate(m):
            if len(bestmoves) > 0 and len(map)+(len(m)-1) == bestmoves[len(bestmoves)-1]:
                break

            temp = [x[:] for x in map]
            if n == 1 or j == 0:
                #temp[i][j] = 0
                nums = []
                nums.append("")
                add = ""
                maze  = createMaze(temp)
                totalMoves = 0
                #print(maze)
                #print(map)
                while True:
                    totalMoves = findEnd(maze, add)
                    if totalMoves != False:
                        bestmoves.append(totalMoves)
                        break
                    else: 
                        add = nums.pop(0)
                        for j in ["L", "R", "U", "D"]:
                            put = add + j
                            if valid(maze, put):
                                nums.append(put)
    bestmoves.sort()
    #print(bestmoves)
    return bestmoves[0]

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))