


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


#Partition algorithm to calculate the median of three numbers using two comparisons
def Partition_Version_4(array, low_index: int, high_index: int):
    swap_count = 0
    comparison_count = 0
    median = ((high_index - 1) - low_index) // 2
    median = median + low_index
    left = low_index + 1
    if (array[median] - array[high_index - 1]) * (array[low_index] - array[median]) >= 0:
        array[median],array[low_index] = array[low_index],array[median]
        swap_count += 1
        comparison_count += 1
    elif (array[high_index - 1] - array[median]) * (array[low_index] - array[high_index - 1]) >=0:
        array[low_index],array[high_index - 1] = array[high_index - 1],array[low_index]
        swap_count += 1
        comparison_count += 1
    pivot = array[low_index]
    for right in range(low_index, high_index):
        if pivot > array[right]:
            array[left],array[right] = array[right],array[left]
            swap_count += 1
            comparison_count += 1
            left = left + 1
    array[low_index], array[left - 1] = array[left - 1], array[low_index]
    swap_count += 1
    comparison_count += 1
    return left - 1, swap_count, comparison_count


