def insertionsort(arr):
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

myarray = [64, 34, 25, 12, 22, 11, 90]
insertionsort(myarray)
for i in range(len(myarray)):
    print(myarray[i])
        
