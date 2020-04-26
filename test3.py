def solution(src, dest):
    upleft = 17
    upright = 15
    downleft = -15
    downright = -17
    
    leftup = 10
    rightup = 6
    leftdown = -6
    rightdown = -10

    traveled = 0
    distance = dest - src
    reached = False
    direction = 1 # 1 - left, 0 - right
    while reached == False:
        destPos = dest % 8
        srcPos = src % 8

        if destPos > srcPos:
            direction = 1
        else:  
            direction = 0

        if remaining > 17:
            traveled = traveled + updown

        if remaining < 17 :
            
