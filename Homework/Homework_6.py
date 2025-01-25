def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(val, arr):
    n = len(arr)
    result_ok = False
    first = 0
    last = n - 1
    pos = -1

    while first <= last:
        middle = (first + last) // 2
        if val == arr[middle]:
            result_ok = True
            pos = middle
            break
        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f"Элемент найден на позиции {pos}")
    else:
        print("Элемент не найден")

numbers = [4,5,3,1,2]
selection_sort(numbers)
print(numbers)
binary_search(2,numbers)