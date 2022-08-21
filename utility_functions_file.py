#this file is for an assortment of needed utility files
#import os
#cwd = os.getcwd()
#files = os.listdir(cwd)
#print("Files in %r: %s" % (cwd, files))
import os

#this function reads a file and converts it into an array
def read_the_file(file_name):
    with open(file_name, 'r') as file_name:
        array = file_name.read().splitlines()
        # puts the file into an array
        array = [eval(i) for i in array]
        return array

#print(read_the_file('Ascending_50_Character.txt'))





