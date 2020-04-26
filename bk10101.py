def solution(map):

    # for i, m in enumerate(map):
    #     for j, n in enumerate(m):
    #         if m.count(0) < 3 and i > 0 and i < len(map)-1:
    #             if n == 1 and (map[i-1][j] == 0 or map[i-1][j] == "2") and map[i+1][j] == 0:
    #                 map[i][j] = 0
    #                 break
    #     #print(m)
    # for i, m in enumerate(map):
    #     for j, n in enumerate(m):
    #         if i < len(m)-2:
    #             #print(str(map[i+1][j]))
    #             if n == 0 and map[i+1][j] == 1 and map[i+2][j] == 0:
    #                 map[i+1][j] = 0
    #                 break

    # print(one)


    def createMaze(map):
        map[0][0] = "2"
        map[len(map)-1][len(map[len(map)-1])-1] = "X"
        return map

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
            elif (maze[j][i] == 1):
                return False
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

    nums = []
    nums.append("")
    add = ""
    maze  = createMaze(map)
    totalMoves = 0
    while True:
        totalMoves = findEnd(maze, add)
        if totalMoves != False:
            break
        else: 
            add = nums.pop(0)
            for j in ["L", "R", "U", "D"]:
                put = add + j
                if valid(maze, put):
                    #print(put)
                    nums.append(put)
    print(add)
    return totalMoves

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))

print(solution([[0, 0, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 1, 0], 
                [1, 1, 0, 0, 0, 1, 0], 
                [1, 1, 0, 1, 0, 1, 0], 
                [1, 0, 0, 1, 0, 0, 0],
                [1, 0, 1, 1, 1, 1, 1], 
                [1, 0, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 1, 0]]))