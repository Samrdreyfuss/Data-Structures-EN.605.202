# Function to perform quicksort for Partition_Version_1 algorithm:(Select the first item of the partition as the pivot)
from Partition import Partition_Version_1

def Iterative_Quick_Sort_Version_1(array, low_index, high_index):
    comparisons = 0
    #create stack and define operational variables
    size = high_index - low_index + 1
    stack = [0] * size
    stack_top = -1
    stack_top = stack_top + 1
    stack[stack_top] = low_index
    stack_top = stack_top + 1
    stack[stack_top] = high_index

    #Pop from stack while stack is NOT empty
    while stack_top >= 0:
        #Pop high_index and low_index
        high_index = stack[stack_top]
        stack_top = stack_top - 1
        low_index = stack[stack_top]
        stack_top = stack_top - 1

        #call Partition function (with respect to version #)
        partition_value = Partition_Version_1(array, low_index, high_index)
        #partition_value = partition_value[1]

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

