def steps(N):
    if N == 0:
        return [()]
    elif N == 1:
        return [(1,)]
    else:
        l1 = [(1,) + items for items in steps(N - 1)]
        l2 = [(2,) + items for items in steps(N - 2)]
        return l1 + l2

print(steps(50))