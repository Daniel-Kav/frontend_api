# def selection_sort(arr):
#     n = len(arr)
#     #traverse through the array
#     for i in range(n):
#         # find the minimum element in the remaining unsorted array
#         min_index = i

#         for j in range(i+1  , n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         # swapp the found minimum element with the first unsorted element
#         arr[i], arr[min_index] = arr[min_index], arr[i]


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 250, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)
