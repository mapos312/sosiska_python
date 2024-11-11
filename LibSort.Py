def bubble_sort(a): 
	n = len(a) 
	unordered = True 
	while unordered: 
		unordered = False 
		for j in range(n - 1): 
			if a[j] > a[j + 1]: 
				a[j], a[j + 1] = a[j + 1], a[j] 
				unordered = True 
	n -= 1 


def selection_sort(a): 
	for i in range(len(a) - 1): 
		imin = i 
		for j in range(i + 1, len(a)): 
			if a[j] < a[imin]: 
				imin = j 
		a[i], a[imin] = a[imin], a[i] 


def insertion_sort(a): 
	for i in range(1, len(a)): 
		tmp = a[i] 
		j = i - 1 
		while j >= 0 and a[j]>tmp: 
			a[j + 1] = a[j] 
			j -= 1 
		a[j + 1] = tmp 


def quick_sort(arr, low, high):
    if low < high:
        # Разделяем массив и находим индекс опорного элемента
        pivot_index = partition(arr, low, high)

        # Рекурсивно сортируем элементы слева и справа от опорного элемента
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # Опорный элемент — первый элемент подмассива
    i = low + 1       # Начинаем с элемента сразу после pivot
    
    for j in range(low + 1, high + 1):
        # Если текущий элемент меньше или равен pivot, перемещаем его в "левую часть"
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    # Помещаем pivot на его правильное место в отсортированном массиве
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1  # Возвращаем индекс pivot


def merge_sort(arr):
    # Последнее разделение массива
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Выполняем merge_sort рекурсивно с двух сторон
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Объединяем стороны вместе
    return merge(left, right, arr.copy())


def merge(left, right, merged):    #сортировка слиянием

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Сортируем каждый и помещаем в результат
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
