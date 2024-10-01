# def insertion_sort(arr):
#     # traverse through 1 o len array
#     for i in range(1,len(arr)):
#         currentNumber = arr[i]
#         prevNumber = i - 1

#         # move elements of arr[0..i-1], that are greater than key to 
#         # one position ahead of their current position
#         while prevNumber >= 0 and currentNumber < arr[prevNumber] :
#             arr[prevNumber + 1] = arr[prevNumber]
#             prevNumber -=1

#         arr[prevNumber +1] = currentNumber

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+  1] = key
arr = [10, 3, 15, 7, 8]
insertion_sort(arr)
print("Sorted array:", arr)