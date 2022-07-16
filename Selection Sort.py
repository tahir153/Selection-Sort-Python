def selection_sort(L):
    for i in range(len(L)-1):
        min = i
        for j in range(i+1, len(L)-1):
            if L[j] < L[min]:
                min = j
        temp = L[i]
        L[i] = L[min]
        L[min] = temp

L = [3, 1, 41, 59, 26, 53, 59]
selection_sort(L)
print(L)

# find min value in array, after every iteration the one minimun value will set in array.