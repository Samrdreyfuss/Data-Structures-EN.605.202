


#Algorithm to find the partition positions for: Version 1 (Select the first item of the partition as the pivot)
def Partition_Version_1(array, low_index, high_index):
    low, high = low_index, high_index
    swap_count = 0
    comparison_count = 0
    #precondition:
    if low_index != high_index and low_index < high_index:
        #define the first element as pivot_point
        pivot_point = array[low_index]
        low += 1
        #Move through array and compare each element with pivot_point
        while low <= high:
            comparison_count +=1
            if array[high] < pivot_point  and array[low] > pivot_point:
                array[high], array[low] = array[low], array[high]
                swap_count += 1

            if not array[low] > pivot_point:
                low += 1
            if not array[high] < pivot_point:
                high -= 1
        #swap pivot element with > element
        array[low_index], array[high] = array[high], array[low_index]
        swap_count += 1
     #Return the position from where partition is done
    return high, swap_count, comparison_count

def Partition_Version_2(array, low_index, high_index):
    low, high = low_index, high_index
    swap_count = 0
    comparison_count = 0
    #precondition:
    if low_index != high_index and low_index < high_index:
        #define the first element as pivot_point
        pivot_point = array[low_index]
        #logic for confirming if partition is equal or over 100 characters, if so use an insertion sort to finish
        low += 1
        #Move through array and compare each element with pivot_point
        while low <= high:
            comparison_count +=1
            if array[high] < pivot_point  and array[low] > pivot_point:
                array[high], array[low] = array[low], array[high]
                swap_count += 1

            if not array[low] > pivot_point:
                low += 1
            if not array[high] < pivot_point:
                high -= 1
            #swap pivot element with > element
        array[low_index], array[high] = array[high], array[low_index]
        swap_count += 1
    #Return the position from where partition is done
    return high, swap_count, comparison_count

def Partition_Version_3(array, low_index, high_index):
    low, high = low_index, high_index
    swap_count = 0
    comparison_count = 0
    #precondition:
    if low_index != high_index and low_index < high_index:
        #define the first element as pivot_point
        pivot_point = array[low_index]
        #logic for confirming if partition is equal or over 100 characters, if so use an insertion sort to finish
        low += 1
        #Move through array and compare each element with pivot_point
        while low <= high:
            comparison_count +=1
            if array[high] < pivot_point  and array[low] > pivot_point:
                array[high], array[low] = array[low], array[high]
                swap_count += 1

            if not array[low] > pivot_point:
                low += 1
            if not array[high] < pivot_point:
                high -= 1
            #swap pivot element with > element
        array[low_index], array[high] = array[high], array[low_index]
        swap_count += 1
    #Return the position from where partition is done
    return high, swap_count, comparison_count

def get_median(a: int, b: int, c: int):
    if (a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

#Partition algorithm to calculate the median of three numbers using two comparisons
def Partition_Version_4(array: list, left_index: int, right_index: int):
    swap_count = 0
    comparison_count = 0
    middle = (right_index + left_index) // 2

    pivot = get_median(array[left_index], array[right_index], array[middle])

    #obtain index pivot
    pivot_index = array.index(pivot)

    array[pivot_index] = array[left_index]
    #swap first item in arry with pivot
    array[left_index] = pivot
    swap_count += 1

    i = left_index + 1
    for j in range(left_index + 1, right_index + 1):
        comparison_count += 1

        if array[j] < pivot:
            swap_count += 1
            array[i], array[j] = array[j], array[i]
            i += 1

    array[left_index], array[i-1] = array[i-1], array[left_index]
    swap_count += 1
    pivot_index = i - 1
    return pivot_index, swap_count, comparison_count





