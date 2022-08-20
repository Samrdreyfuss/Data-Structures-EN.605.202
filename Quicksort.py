# Function to perform quicksort for Partition_Version_1 algorithm:(Select the first item of the partition as the pivot)
from Partition import Partition_Version_1, Partition_Version_2

#Insersion sort logic used for Version 2 and 3
def Insertion_Sort(array) -> tuple:
    comparison_count = 0
    swap_count = 0
    for index in range(1, len(array)):
        comparison_count += 1
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            swap_count += 1
            array[position] = array[position - 1]
            position = position - 1
        array[position] = current_value
    return array, comparison_count, swap_count

#Quicksort Version 1 ****************************************************
def Iterative_Quick_Sort_Version_1(array, low_index, high_index) -> tuple:
    #create stack (from scratch!) and define operational variables
    size = high_index - low_index + 1
    stack = [0] * size
    stack_top = -1
    stack_top = stack_top + 1
    stack[stack_top] = low_index
    stack_top = stack_top + 1
    stack[stack_top] = high_index
    comparison_count = 0
    swap_count = 0

    #Pop from stack while stack is NOT empty
    while stack_top >= 0:
        #Pop high_index and low_index
        high_index = stack[stack_top]
        stack_top = stack_top - 1
        low_index = stack[stack_top]
        stack_top = stack_top - 1

        #call Partition function (with respect to quicksort version #)
        partition_value, swap_count_child, comparison_count_child = Partition_Version_1(array, low_index, high_index)
        comparison_count += comparison_count_child
        swap_count += swap_count_child

        #algorithm will push left side onto stack
        if partition_value - 1 > low_index:
           stack_top = stack_top + 1
           stack[stack_top] = low_index
           stack_top = stack_top + 1
           stack[stack_top] = partition_value - 1

        #algorithm will push right side onto stack
        if partition_value + 1 < high_index:
           stack_top = stack_top + 1
           stack[stack_top] = partition_value + 1
           stack_top = stack_top + 1
           stack[stack_top] = high_index

    if len(array) == 50:
        print('Sort Function: Quicksort Version 1')
        print('Sorted Array: ', array)
        print('Swap Count: ', swap_count)
        print('Comparison Count: ', comparison_count)
        print('\n')
    else:
        print('Sort Function: Quicksort Version 1')
        print('Swap Count: ', swap_count)
        print('Comparison Count: ', comparison_count)
        print('\n')

    return array, swap_count, comparison_count


#Quicksort Version 2 ****************************************************
def Iterative_Quick_Sort_Version_2(array, low_index, high_index) -> tuple:
    #create stack (from scratch!) and define operational variables
    size = high_index - low_index + 1
    stack = [0] * size
    stack_top = -1
    stack_top = stack_top + 1
    stack[stack_top] = low_index
    stack_top = stack_top + 1
    stack[stack_top] = high_index
    comparison_count = 0
    swap_count = 0

    #Pop from stack while stack is NOT empty
    while stack_top >= 0:
        #Pop high_index and low_index
        high_index = stack[stack_top]
        stack_top = stack_top - 1
        low_index = stack[stack_top]
        stack_top = stack_top - 1

        #call Partition function (with respect to quicksort version #2)
        partition_value, swap_count_child, comparison_count_child = Partition_Version_2(array, low_index, high_index)
        comparison_count += comparison_count_child
        swap_count += swap_count_child

        #algorithm will push left side onto stack
        if partition_value - 1 > low_index:
            if high_index - low_index <= 100:
                array, comparison_count, swap_count = Insertion_Sort(array)
                comparison_count += comparison_count_child
                swap_count += swap_count_child
            else:
                stack_top = stack_top + 1
                stack[stack_top] = low_index
                stack_top = stack_top + 1
                stack[stack_top] = partition_value - 1

        #algorithm will push right side onto stack
        if partition_value + 1 < high_index:
           stack_top = stack_top + 1
           stack[stack_top] = partition_value + 1
           stack_top = stack_top + 1
           stack[stack_top] = high_index

    if len(array) == 50:
        print('Sort Function: Quicksort Version 2')
        print('Sorted Array: ', array)
        print('Swap Count: ', swap_count)
        print('Comparison Count: ', comparison_count)
        print('\n')
    else:
        print('Sort Function: Quicksort Version 2')
        print('Swap Count: ', swap_count)
        print('Comparison Count: ', comparison_count)
        print('\n')

    return array,swap_count,comparison_count



#array = [9,0,8,1,7,3,6,4,10,20,5,14]
#Iterative_Quick_Sort_Version_2(array, 0, len(array) - 1)

