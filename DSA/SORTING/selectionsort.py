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


# def selection_sort(arr):
#     n = len(arr)
#     comparison_count = 0

#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             comparison_count += 1

#             if arr[j][1] < arr[min_index][1]:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return comparison_count

def selection_sort(arr):

    n = len(arr)
    for i in range(n):

        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 250, 120, 22, 11,49,2,9,3,1]
# arr = ["apple", "orange", "banana", "grape"]
# arr = [(2, 3), (1, 5), (4, 2)]
print(selection_sort(arr))
print("Sorted array is:", arr)
