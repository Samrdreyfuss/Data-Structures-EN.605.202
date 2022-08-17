'''
This method generates 15 input files needed for the lab:

3 versions of each file (ascending, decending, and random)
'''

from random import randint, shuffle

def Create_File(filename: str, size: int, ascending: bool, random: bool):
    with open(filename, 'w') as file:
        if ascending:
            for i in range(size):
                if i == size - 1:
                    file.write(str(i))
                else:
                    file.write(str(i) + '\n')
        elif random:
            array = list(range(size))
            shuffle(array)
            for i in range(len(array)):
                if i == size - 1:
                    file.write(str(array[i]))
                else:
                    file.write(str(array[i]) + '\n')
        else:
            for i in range(size):
                for i in range(size):
                    if i == size - 1:
                        file.write(str(size - i))
                    else:
                        file.write(str(size - i) + '\n')

def Create_Multiple_Files():
    for size in [10000, 5000, 2000, 1000, 50]:
        Create_File('Ascending_' + str(size) + '.txt', size, True, False)
        Create_File('Descending_' + str(size) + '.txt', size, False, False)
        Create_File('Random_' + str(size) + '.txt', size, True, True)

