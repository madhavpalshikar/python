def solution(map):

    rangeList = []
    onlyOnesList = 0
    for j, x in enumerate(map):
        rangeList.append([])
        rangeList[j] = []
        setx = []
        start = -1
        end = -1
        zeroFound = False
        for i, y in enumerate(x):
            if y == 0 and start == -1:
                zeroFound = True
                start = i
                end = i
                print('start', i)
            elif y == 0:
                zeroFound = True
                end = i 
                print('end', i)
            else:
                if start > -1 and end > -1:
                    setx.append(start)
                    setx.append(end)
                    rangeList[j].append(setx)
                    start = -1
                    end = -1
                    setx = []
                    #print(j)
        else:
            if start > -1 and end > -1:
                setx.append(start)
                setx.append(end)
                rangeList[j].append(setx)
                start = -1
                end = -1
                setx = []
            elif zeroFound == False:
                start = -1
                end = -1
                setx.append(start)
                setx.append(end)
                rangeList[j].append(setx)
                setx = []
                onlyOnesList = onlyOnesList + 1

    if onlyOnesList > 0:
        for i, x in enumerate(rangeList):
            print(x)
    print(rangeList)
    return True

#solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
