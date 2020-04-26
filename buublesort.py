def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

myarray = [64, 34, 25, 12, 22, 11, 90]
bubblesort(myarray)

for k in range(len(myarray)):
    print(myarray[k])

