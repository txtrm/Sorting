Ar1 = [2, 0, 100, 129]

UnsortedArray = Ar1.copy()

def BubbleSort(array):
    made_a_swap = True
    n = len(array)

    while made_a_swap:
        made_a_swap = False

        for i in range(n-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                made_a_swap = True

    return array
    
print(UnsortedArray, "-->", BubbleSort(Ar1))