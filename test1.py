def solution(i):
    primes = ''
    endrange = i + 5
    k = 0
    while len(primes) < endrange:
        k = k + 1
        if k > 1: 
            for x in range(2,k):
                print(k, x)
                if (k % x) == 0:
                    #this is a not a prime number
                    print('not prime', k)
                    break;
            else:
                primes = primes + str(k);
        print(primes)
    return primes[i:endrange]

print(solution(3))