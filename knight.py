def solution(src, dest):
    x = src % 8
    y = int(src / 8)

    tx = dest % 8
    ty = int(dest / 8)
    print (x, y, tx, ty)
    dp = [[0 for i in range(8)] for j in range(8)]; 

    def calculateStep(x, y, tx, ty):
        if (x == tx and y == ty): 
            return dp[0][0]; 

        elif(dp[abs(x - tx)][abs(y - ty)] != 0): 
            return dp[abs(x - tx)][abs(y - ty)]; 
        else: 

            x1, y1, x2, y2 = 0, 0, 0, 0; 
            if (x <= tx): 
                if (y <= ty): 
                    x1 = x + 2; 
                    y1 = y + 1; 
                    x2 = x + 1; 
                    y2 = y + 2; 
                else: 
                    x1 = x + 2; 
                    y1 = y - 1; 
                    x2 = x + 1; 
                    y2 = y - 2; 

            elif (y <= ty): 
                x1 = x - 2; 
                y1 = y + 1; 
                x2 = x - 1; 
                y2 = y + 2; 
            else: 
                x1 = x - 2; 
                y1 = y - 1; 
                x2 = x - 1; 
                y2 = y - 2; 

            dp[abs(x - tx)][abs(y - ty)] = min(calculateStep(x1, y1, tx, ty), calculateStep(x2, y2, tx, ty)) + 1; 
            dp[abs(y - ty)][abs(x - tx)] = dp[abs(x - tx)][abs(y - ty)]; 
            return dp[abs(x - tx)][abs(y - ty)]; 
            
    n = 64; 

    if ((x == 1 and y == 1 and tx == 2 and ty == 2) or
            (x == 2 and y == 2 and tx == 1 and ty == 1)): 
        ans = 4; 
    elif ((x == 1 and y == n and tx == 2 and ty == n - 1) or
        (x == 2 and y == n - 1 and tx == 1 and ty == n)): 
        ans = 4; 
    elif ((x == n and y == 1 and tx == n - 1 and ty == 2) or
        (x == n - 1 and y == 2 and tx == n and ty == 1)): 
        ans = 4; 
    elif ((x == n and y == n and tx == n - 1 and ty == n - 1) 
        or (x == n - 1 and y == n - 1 and tx == n and ty == n)): 
        ans = 4; 
    else: 

        dp[1][0] = 3; 
        dp[0][1] = 3; 
        dp[1][1] = 2; 
        dp[2][0] = 2; 
        dp[0][2] = 2; 
        dp[2][1] = 1; 
        dp[1][2] = 1; 
        return calculateStep(x, y, tx, ty)
    

print(solution(1,63));
