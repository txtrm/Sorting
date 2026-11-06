import random

Ar1 = [2, 0, 100, 12]

def BogoSort(array):
    is_sorted = all(array[i] <= array[i+1] for i in range(len(array)-1))

    while not is_sorted:
        random.shuffle(array)
        is_sorted = all(array[i] <= array[i+1] for i in range(len(array)-1))
    
    return array

print(BogoSort(Ar1))