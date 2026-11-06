Ar1 = [2, 0, 100, 129]

def InsertionSort(array):
    Ar2 = []
    Ar2.append(array[0])
    del array[0]

    for i in range(len(array)):
        n2 = len(Ar2)
        found = False

        for j in range(n2):
            if Ar2[j] > array[0]:
                Ar2.insert(j, array[0])
                del array[0]
                found = True
                break
        if not found:        
            Ar2.append(array[0])
            del array[0]

    return Ar2

print(InsertionSort(Ar1))