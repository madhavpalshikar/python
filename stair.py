def solution(n):

    def findcount(n):
        count = 1
        stairs = [n-1, 1]
        print(stairs)
        max = False
        loop = 0
        while max == False:
            temp = count
            i = 0
            while i < len(stairs):
                if(i < len(stairs)-1):
                    if stairs[i] == stairs[i+1]:
                        if stairs[i+1] != 1 :
                            stairs[0] = stairs[0] + 1
                            # stairs.append(1)
                            count = count + 1

                    if (stairs[i+1] < stairs[i]-1):
                        
                        if stairs[i] - stairs[i+1] > 1:
                            stairs[i] = stairs[i] - 1
                            stairs[i+1] = stairs[i+1] + 1
                            count = count + 1
                        
                        if stairs[i] - stairs[i+1] == 2 and stairs[len(stairs)-1] !=0 : 
                            if stairs[i+1] != 1 :
                                stairs.append(0)
                                print(str(stairs[i+1])+'################################')
                            else:
                                max = True
                            # stairs[i] = stairs[i] - 1
                            # stairs.append(1)
                            # count = count + 1
                        elif stairs[i] - stairs[i+1] == 1 and stairs[i+1] != 1 and stairs[len(stairs)-1] !=0:
                            print(str(stairs[i+1])+'-----------------------------------')
                            stairs.append(0)

                        # print(stairs[i], stairs[i+1])
                        # if stairs[i] == 2 and stairs[i+1] == 1:
                        # max = True
                        
                i = i + 1
                print('while loop', i)
                if temp == count:
                    loop = loop + 1
                else:
                    loop = 0
                if loop > 10:
                    max = True
            print(count) 
            print(stairs)
            #max = True
        print(max)
        return count


    count = 1
    stairs = [n-1, 1]
    print(stairs)
    max = False
    loop = 0
    while max == False:
        temp = count
        i = 0
        while i < len(stairs):
            if(i < len(stairs)-1):
                if stairs[i] == stairs[i+1]:
                    if stairs[i+1] != 1 :
                        stairs[0] = stairs[0] + 1
                        # stairs.append(1)
                        count = count + 1

            

                if (stairs[i+1] < stairs[i]-1):
                    
                    if stairs[i] - stairs[i+1] > 1:
                        stairs[i] = stairs[i] - 1
                        stairs[i+1] = stairs[i+1] + 1
                        count = count + 1
                    

                    if stairs[i] - stairs[i+1] == 2 and stairs[len(stairs)-1] !=0 : 
                        if stairs[i+1] != 1 :
                            stairs.append(0)
                            print(str(stairs[i+1])+'################################')
                            childCount = findcount(stairs[i+1])
                            count = count + childCount
                        else:
                            max = True
                        # stairs[i] = stairs[i] - 1
                        # stairs.append(1)
                        # count = count + 1
                    elif stairs[i] - stairs[i+1] == 1 and stairs[i+1] != 1 and stairs[len(stairs)-1] !=0:
                        print(str(stairs[i+1])+'-----------------------------------')
                        stairs.append(0)
                        childCount = findcount(stairs[i+1])
                        count = count + childCount
                    # print(stairs[i], stairs[i+1])
                    # if stairs[i] == 2 and stairs[i+1] == 1:
                    # max = True
                    
            i = i + 1
            print('while loop', i)
            if temp == count:
                loop = loop + 1
            else:
                loop = 0
            if loop > 10:
                max = True
                
        print(count)     
        print(stairs)
        #max = True
    print(max)
    return count    

print(solution(200))
