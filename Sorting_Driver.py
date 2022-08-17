'''
Sam Dreyfuss - Data Structures - Sorting Analysis - August 2022
Sources:
1.https://www.youtube.com/watch?v=8hHWpuAPBHo
2.https://learn.zybooks.com/zybook/JHUEN605202PythonSummer2022/chapter/7/section/16
3.Problem Solving with Algorithms and Data Structures, Miller and Ranum
4. CAREFUL - https://www.geeksforgeeks.org/quick-sort/
5. CAREFUL - https://www.studytonight.com/python-programs/python-program-for-iterative-quicksort (manual stack)
'''

from Quicksort import Iterative_Quick_Sort_Version_1

#Driver code
if __name__ == '__main__':
    print('Code Running As Expected')


    # Driver code
    array = [9,0,8,1,7,3,6,4,10,20,5,14,6,8,9,10,5,1,2]
    Iterative_Quick_Sort_Version_1(array, 0, len(array) - 1)
    #swap_count_final_value =

    print(f'Sorted array: {array}')





