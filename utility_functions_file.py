#this file is for an assortment of needed utility files
#import os
#cwd = os.getcwd()
#files = os.listdir(cwd)
#print("Files in %r: %s" % (cwd, files))

#this function reads a file and converts it into an array
def read_the_file(file_name):
    import os
    with open(file_name, 'r') as file_name:
        array = file_name.read().splitlines()
        # puts the file into an array
        array = [eval(i) for i in array]
        return array





