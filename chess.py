def solution(src, dest):
    if src > dest:
        temp = src
        src = dest
        dest = temp

    upleft = 17
    upright = 15
    leftup = 10
    rightup = 6

    downleft = -15
    downright= -17
    leftdown = -6
    rightdown = -10

    possibleSteps = [17, 15, 10, 6, -15, -17, -6, -10]

    direction = 1 

    steps = 0
    travelled = 0
    distance = dest - src
    currentLocation = src
    #print(distance)

    while currentLocation != dest:
        
        if (currentLocation % 8) > (dest % 8):
            direction = 0
        else:
            direction = 1
        distance = dest - currentLocation

        if distance == 5:
            steps = steps + 3
            currentLocation = dest
            break

        if currentLocation % 8 == 0 and currentLocation + 7 == dest:
            currentLocation = dest
            steps = steps + 5
            break
        if (currentLocation+1) % 8 == 0 and currentLocation + 1 == dest:
            currentLocation = dest
            steps = steps + 4
            break    
        if distance == 1 or distance == 8:
            if(steps > 0):
                steps = steps - 1
            currentLocation = dest
            steps = steps + 3
            break  
        if distance == 7 or distance == 9:
            currentLocation = dest
            steps = steps + 2
            break 
            
        for x in possibleSteps:           
            if currentLocation+x == dest:
                currentLocation = dest
                steps = steps + 1
                #print(x)
                break
        else:
            #currentLocation = currentLocation + 17
            
            if direction==1 :
                if distance == 11 or distance == 7 or distance == 9 or distance == 5:
                    steps = steps + 2
                    currentLocation = dest

                if distance == 12:
                    steps = steps + 3
                    currentLocation = dest

                if (currentLocation + 1) % 8 == 0:
                    direction = 0

                if currentLocation < 47 and (currentLocation + 1) % 8 != 0:
                    currentLocation = currentLocation + 17
                    steps = steps + 1
                elif currentLocation < 54 and (currentLocation + 2) % 8 != 0 and (currentLocation + 1) % 8 != 0:
                    currentLocation = currentLocation + 10
                    steps = steps + 1

            if direction==0:
                if distance == 11 or distance == 7 or distance == 9 or distance == 5:
                    steps = steps + 2
                    currentLocation = dest

                if distance == 12:
                    steps = steps + 3
                    currentLocation = dest

                if currentLocation % 8 == 0:
                    direction = 1

                if currentLocation < 48 and currentLocation % 8 != 0:
                    currentLocation = currentLocation + 15
                    steps = steps + 1
                elif currentLocation < 56 and currentLocation % 8 != 0 and (currentLocation + 1) % 8 != 0:
                    currentLocation = currentLocation + 6
                    steps = steps + 1
        
    print(str(src)+'--->'+str(dest))        
    return steps
print(solution(0,17))
print(solution(17,27))
print(solution(1,2))
print(solution(1,9))
print(solution(1,10))
print(solution(48, 55))
print(solution(55, 56))
print(solution(19,36))
print(solution(0,1))
print(solution(5,23))
print(solution(1,44))
print(solution(1,45))
print(solution(45,1))
print(solution(0, 63))

print(solution(40,49))
print(solution(3,59))
print(solution(2,58))
print(solution(12,33))
print(solution(41,46))
print(solution(34,42))
print(solution(4,62))
print(solution(7,63))
