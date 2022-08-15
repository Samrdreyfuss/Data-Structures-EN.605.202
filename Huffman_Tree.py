''' Sam Dreyfuss - Data Structures - Huffman Encoding - August 2022
Sources: https://learn.zybooks.com/zybook/JHUEN605202PythonSummer2022/chapter/8/section/11
Problem Solving with Algorithms and Data Structures, Miller and Ranum

I created this algorithm to generate a Huffman tree for the purpose of encoding/compressing data strings.
For example the letter 'E' would typically have 8 bit ASCII value of '0110101'. Utilizing a huffman tree and the given
frequency table, we can convert this letter into a code which only take up 3 bits: '010'. This type of compression allows
us so save such objects as text, JPEG, PNG, and even MP3s files in a fraction of the space we would otherwise need without
compresion.

The algorithm allows the user to specify how they would like to use the software, by choosing to either encode, decode, or
traverse the nodes of the tree using values e,d, or t respectively. The algorithm creates a huffman tree by creating a
leaf node or internal node for each unique charcter within our priority que file. We beging by using a the two rows
with the lowest frequency and create an internal node whose frequency count is equal to the sum of the two min node count
lowest value will be left node, and second lowest will be right node. We repeat this logic until there is only one node
left which we call the root node.

All outputs are printed to both the terminal and specified output.txt file.
'''

#inport string functionality (as permited in the lab instructions ;)
import string

#Create hoffman node class utilizing frequency, character, left child, and right child parameters
class Node:
    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right
    #this method creates print functionality of node class
    def print_node(self):
        print('Frequency:', self.frequency)
        print('Character:', self.character)
        print('Left Child:', self.left)
        print('Right Child:', self.right)

#this algorithm converts a predetermined frequency table to a dictionary (k=keys, v=values)
def Get_Frequency_Dict(frequency_table_file):
    frequency_dict = {}
    with open(frequency_table_file, 'r') as file:
        for line in file:
            if line == '\n':
                continue
            # extract new line from given file
            line = line.strip()
            line = line.replace(' ','')
            k, v = line.split('-')
            frequency_dict[k] = int(v)
            # if there are any blank lines within .txt file, ignore them
    return frequency_dict

#The create tree algorithm (using a chosen frequency table argument) creates a tree structure
def Create_Tree(frequency_dict):
    nodes = []
    #converting characters and counts into huffman tree nodes
    for character in frequency_dict:
        nodes.append(Node(frequency_dict[character], character, None, None))

    while len(nodes) > 1:
        #sort all the nodes by frequency
        nodes = sorted(nodes, reverse=False,key=lambda x: x.frequency)
        #choose two smallest nodes to begin the building of the bottom of the tree
        left = nodes[0]
        right = nodes[1]

        # combining 2 nodes to create new node
        new_node = Node(left.frequency + right.frequency, left.character + right.character, left, right)
        nodes.pop(0)
        nodes.pop(0)
        nodes.append(new_node)
        #sort nodes by frequency
        nodes = sorted(nodes, reverse=False, key=lambda x: x.frequency)
    return nodes[0]

#The below algorithm uses the previously created huffman tree structure to generate a code by traversing
def Create_Huffman_Codes(node, text_input,file_out):
    coded_output = ''
    #convert string to uppercase
    text_input = text_input.upper()
    # remove punctuation from string text input
    text_input = text_input.replace('!', '')
    text_input = text_input.replace('.', '')
    text_input = text_input.replace('?', '')
    text_input = text_input.replace(',', '')
    text_input = text_input.replace(' ', '')

    for character in text_input:
        #create blank character code variable to keep track of char codes
        char_code = ''
        #remove spaces
        if character == ' ':
            continue
        current_node = node
        #once only one node is left, exit the while loop (the remaining node will be the root node)
        while len(current_node.character) > 1:
            #determine left code
            if character in current_node.left.character:
                current_node = current_node.left
                coded_output += '0'
                char_code += '0'
                continue
            else:
                #determine right code
                current_node = current_node.right
                coded_output += '1'
                char_code += '1'
                continue
        char_code = char_code
        #print to terminal
        print('Character:', current_node.character, '  Code:', char_code)
        #print to file
        with open(file_out, 'a') as path:
            # print to file
            print('Character:', current_node.character, '  Code:', char_code, file=path)
    #return tuple of coded output and lenth of coded output for additional computation of storage savings
    return coded_output, 'Length:',len(coded_output)

#this algorithm takes a coded text intput (example: '010') and converts it to a readable letter (example: 'E')
def Decompress_Huffman_Code(text_input, node):
    output = []
    tree_head = node
    for char in text_input:
        if char == '1':
            node = node.right
        elif char == '0':
            node = node.left
        try:
            if node.left.character == None and node.right.character == None:
                continue
        except AttributeError:
            output.append(node.character)
            node = tree_head
    decoded_output = ''.join([str(code) for code in output])
    return decoded_output

#this algorithm prints out each node and frequency value in a preorder order
def Print_Preorder_Traversal(node,file_out):
    # if root is None,return
    if node is None:
        return
        print('Root is Empty')
    # print the current node
    print('Node:',node.character,'  Freq:', node.frequency)
    with open(file_out, 'a') as path:
        # print to file
        print('Node:',node.character,'  Freq:', node.frequency, file=path)
    #travel left node recursively
    Print_Preorder_Traversal(node.left,file_out)
    #travel right node recursively
    Print_Preorder_Traversal(node.right,file_out)

#this algorithm prints out the binary/8 bit version of a given character for a Huffman compression comparison
def Compute_Binary_Conversion(input_string):
    #remove punctuation from string
    input_string = input_string.replace('!', '')
    input_string = input_string.replace('.', '')
    input_string = input_string.replace('?', '')
    input_string = input_string.replace(',', '')
    input_string = input_string.replace(' ', '')
    res = ''.join(format(ord(i), '08b') for i in input_string)
    return res,' - Length:',len(res)

#driver for code. Below is the logic to be entered by user and cordinated/appropriate logic returned from algorithm
if __name__ == '__main__':
    #confirm code is running
    print('Code Running As Expected')
    #user text input
    use_case = input('How Would You Like To Use This Software? (e=encode, d=decode, t=traverse tree): ')
    #user text input
    file_out = input('Please Enter The Name Of The Output File You Wish To Save In Your Working Folder (o=Output.txt): ')
    if file_out == 'o':
        file_out = '../../Desktop/Hopkins 2022/Data Structures/DreyfussSamLab3/Output.txt'
    else:
        file_out = file_out

    # user text input
    frequency_file = input('Please Enter The Name Of The Frequency File You Would Like To Convert To A Tree (f=FreqTable.txt): ')

    if frequency_file == 'f':
        frequency_file = '../../Desktop/Hopkins 2022/Data Structures/DreyfussSamLab3/FreqTable.txt'
    else:
        frequency_file = frequency_file

    freq_table_file_dict = Get_Frequency_Dict(frequency_file)
    node = Create_Tree(freq_table_file_dict)

    if use_case == 't':
        use_case

        print('***Traversing (Preorder)***')
        with open(file_out, 'a') as path:
            # print to file
            print('***Traversing (Preorder)***', file=path)
        Print_Preorder_Traversal(node,file_out)

    # user text input
    if use_case == 'e':
        # user text input
        file_in = input('Please Enter The File You Would Like To Compress (c=ClearText): ')

        if file_in == 'c':
            file_in = '../../Desktop/Hopkins 2022/Data Structures/DreyfussSamLab3/ClearText.txt'
        else:
            file_in = file_in
        print('***Encoding***')
        with open(file_out, 'a') as path:
            # print to file
            print('***Encoding***', file=path)

        with open(file_in, 'r') as file:
            for line in file:
                print('Converting This String: ', line)
                line_2 = line
                with open(file_out, 'a') as path:
                    # print to file
                    print('Converting This String: ', line, file=path)
                # if there are any blank lines within .txt file, ignore them
                if line == '\n':
                    continue

                line = line.translate({ord(c): None for c in string.whitespace})
                print(line)

                text_input = line
                binary_codes = Compute_Binary_Conversion(text_input)
                huffman_codes = Create_Huffman_Codes(node, text_input,file_out)
                print('Final Encoded Output: ', *huffman_codes)
                with open(file_out, 'a') as path:
                    # print to file
                    print('Final Encoded Output: ', *huffman_codes, file=path)
                print('You Converted this sentence: ', line_2)
                with open(file_out, 'a') as path:
                    # print to file
                    print('You Converted this sentence: ', line_2, file=path)
                print('By Utilizing Huffman Encoding You Saved', binary_codes[2] - huffman_codes[2],'Bits Of Memory - Or', float((binary_codes[2] - huffman_codes[2])/8),'Bytes')
                with open(file_out, 'a') as path:
                    # print to file
                    print('By Utilizing Huffman Encoding You Saved', binary_codes[2] - huffman_codes[2],'Bits Of Memory - Or', float((binary_codes[2] - huffman_codes[2])/8),'Bytes', file=path)
    if use_case == 'd':
        #user text input
        file_in = input('Please Enter The File You Would Like To Decode (e=Encoded.txt): ')
        if file_in == 'e':
            file_in = '../../Desktop/Hopkins 2022/Data Structures/DreyfussSamLab3/Encoded.txt'
        else:
            file_in
        print('***Decoding***')
        with open(file_out, 'a') as path:
            # print to file
            print('***Decoding***', file=path)
        with open(file_in, 'r') as file:
            for line in file:
                # extract new line from given file
                # line = line.strip()
                # line = line.readline()
                if line != '\n':
                    print('Decompressing this string code: ', line)
                    with open(file_out, 'a') as path:
                        # print to file
                        print('Decompressing this string code: ', line, file=path)
                    # if there are any blank lines within .txt file, ignore them
                    if line == '\n':
                        continue
                    text_input = line
                    decompressed = Decompress_Huffman_Code(text_input, node)
                    print('After Decompression:', decompressed)
                    with open(file_out, 'a') as path:
                        # print to file
                        print('After Decompression:', decompressed, file=path)




