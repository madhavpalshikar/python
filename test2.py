def solution(l):
    l.sort(reverse = True)
    ogl = []
    source = l[:]
    ogl = l[:]
    found = False
    while found == False:
        for x in range(0,len(ogl)):
            s_str = [str(i) for i in ogl]
            i_str = "".join(s_str)
            new_number = int(i_str)
            if(new_number % 3 == 0):
                found = True
            else:
                ogl = source[:]
                print(x, l, ogl, (len(ogl)-1)-x)
                ogl.pop((len(ogl)-1)-x)
            print('for...loop', x)
        print('while loop')
        source.pop()
        if len(source) == 0:
           found = True
           new_number = 0
    return new_number        

print(solution([3,1,4,1,5]))
print(solution([3,1,4,1,5,9]))        

# print(solution([1,1,1,1,1,1,1,1]))
# print(solution([2,2,2,2,2,2,2,2]))