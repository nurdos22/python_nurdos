def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"Элемент {target} найден на индексе {mid}."
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return f"Элемент {target} не найден"

unsorted_list = [7, 5, 4, 2]
print("Исходный список:", unsorted_list)

sorted_list = selection_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

search_element = 5
result = binary_search(sorted_list, search_element)
print(result)
