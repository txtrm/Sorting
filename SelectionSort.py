Ar1 = [4,7,2,8,15,3]
UnsortedArray = Ar1.copy()

def SelectionSort(array):
    n = len(array)
    Smallest = array[1]
    SmallestI = 1

    for j in range(n-1):
        Smallest = array[j]
        SmallestI = j
        for i in range(n-j):
            if array[j+i] < Smallest:
                Smallest = array[j+i]
                SmallestI = j+i
                
        temp = array[j]
        array[j] = Smallest
        array[SmallestI] = temp

    return array

print(UnsortedArray, "-->", SelectionSort(Ar1))
