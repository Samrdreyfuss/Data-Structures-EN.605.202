


#Algorithm to find the partition positions for: Version 1 (Select the first item of the partition as the pivot)
def Partition_Version_1(array, low_index, high_index):
  low, high = low_index, high_index
  swap_count = 0
  #precondition:
  if low_index != high_index and low_index < high_index:
    #define the first element as pivot_point 
    pivot_point = array[low_index]
    low += 1
    #Move through array and compare each element with pivot_point 
    while low <= high:
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
  # Return the position from where partition is done
  return high, swap_count



