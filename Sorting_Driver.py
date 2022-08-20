'''
Sam Dreyfuss - Data Structures - Sorting Analysis - August 2022
Sources:
1.https://www.youtube.com/watch?v=8hHWpuAPBHo
2.https://learn.zybooks.com/zybook/JHUEN605202PythonSummer2022/chapter/7/section/16
3.Problem Solving with Algorithms and Data Structures, Miller and Ranum
4.https://www.geeksforgeeks.org/quick-sort/
5.https://www.studytonight.com/python-programs/python-program-for-iterative-quicksort (manual stack)
'''

from Quicksort import Iterative_Quick_Sort_Version_1
import os
from utility_functions_file import read_the_file
from Quicksort import Iterative_Quick_Sort_Version_1, Iterative_Quick_Sort_Version_2

#Driver code
if __name__ == '__main__':
    print('Code Running As Expected')

    #search for .txt files and append to list
    all_files = []
    for files in os.listdir():
        if files.endswith('.txt'):
            all_files.append(files)
        else:
            continue
    split_files = []
    for file in all_files:
        split_file = file.split('_')
        split_file = split_file[:-1]
        split_file[1] = int(split_file[1])
        split_files.append(split_file)

    sorted_files = sorted(split_files, key=lambda x: (x[0], x[1]))

    for file_data in sorted_files:
        file_type = file_data[0]
        file_size = file_data[1]
        file_name = file_type + '_' + str(file_size) + '_' + 'Character.txt'

        #For quicksort version 1:
        array = read_the_file(file_name)
        print('File Name: ', file_name,'...................................................')
        function_list = [Iterative_Quick_Sort_Version_1(array, array[0], len(array) - 1), Iterative_Quick_Sort_Version_2(array, array[0], len(array) - 1)]
        for function in function_list:
            array = array











