"""
Data Structures, Lab 1 - Creating a Stack (prefix to postfix conversion)- Sam Dreyfuss
Reference for some coding structure: Problem Solving with Algorithms and Data Structures, Miller and Ranum

Below you will find a stack class with push, pop, and size methods (while we don't have to specifically use a class
because we are allowed to use list functionality, I thought it would be fun to create a stack class for this assignment!)
The stack class is used to define and store the stack's operators and operands.
"""
class Stack():
    #my change 2
    def __init__(self):
        self.items = []
    #The push method adds new elements onto the stack
    def push(self, item):
        self.items.append(item)
    #The pop method removes the "top" element from the stack
    def pop(self):
        return self.items.pop()
    #The size method provides to number of elements currently on an instance of a stack
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []
    def peek(self):
        return self.items[0]

'''
#Define reverse method for reversing a stack so that we can read prefix notation "right to left". In the event that we 
want to build out functionality to our code and perhaps include for example: an infix to postfix conversion, having this
function as a module will be useful
'''
def reverse(data):
    return data[::-1]

"""
I created the prefix_to_postfix method to convert prefix notation to postfix notation for files which can be referenced 
dynamically ("Required Input.txt" or "Test_Case.txt"). Utilizing a stack ADT, the algorithm pushes operands onto the 
stack and pops the stack 2 times when it recognizes a predefined operator value.
When the pop method is executed, the popped element is then pushed back onto the stack. 
"""
def prefix_to_postfix(data):
    #call stack class and create instance of stack
    stack = Stack()
    #define operators
    operators = ['+', '-', '*', '/', '$']

    for i in data:
        #convert "^" to "$" (for uniformity of exponentials)
        if i == '^':
            with open('Output.txt', 'a') as path:
                # print to file
                print('Algorithm Recognized ^ and is converting to $', file=path)
            # print to terminal
            print('Algorithm Recognized ^ and is converting to $')
            i = '$'
        #confirm prefix syntax only includes "valid" characters (including alpha and numeric characters). If an invalid
        # character (such as a space) is found, print error flag
        if (ord(i) not in range(65,91)) and (ord(i) not in range(97,123)) and ord(i) not in range(48,58) and (i not in operators):
            #if error is found, print message to file in addition to printing to terminal
            with open('Output.txt', 'a') as path:
                # print to file
                print('Please Check For Correct Character Syntax In Prefix Notation', file=path)
            # print to terminal
            print('Please Check For Correct Character Syntax In Prefix Notation')
            #the driver will stop
            return False

        #check if prefix data line/element is in OPERATOR list.
        if i in operators:
            #Confirm if stack size is less than 2 for stack logic validity/syntax error checking purposes
            #Otherwise print there are not enough operands and call on peek method to show user how far the stack got
            #before the error was recognized. Print the peek method to terminal as well as to output file
            if stack.size() < 2:
                with open(file_out, 'a') as path:
                    #print to file
                    print('Not Enough Operands, Please Check Prefix Notation Structure', file=path)
                    print('Check Size To See How Far The Stack Was Stacked Before Error Was Returned:',stack.size(), file=path)
                # print to terminal
                print('Not Enough Operands, Please Check Prefix Notation Structure')
                print('Check Size To See How Far The Stack Was Stacked Before Error Was Returned:',stack.size())
                return False

            #pop 2 elements from stack
            operand_1 = stack.pop()
            operand_2 = stack.pop()

            #combine operand 1&2 with operator
            temp_table = operand_1 + operand_2 + i

            #push results to stack
            stack.push(temp_table)

            #check if data is OPERAND
        else:
            #push OPERAND to stack
            stack.push(i)
            #print current stack output
    with open('Output.txt', 'a') as path:
        print("Postfix Notation: ", *stack.items,'\n', file=path)
    print("Postfix Notation: ", *stack.items, '\n')


#define a single driver to execute code - let user know if code is "Running as Expected":
if __name__ == '__main__':
    print('Code Running As Expected')

    # ask user for input file name ("Required Input.txt" or "Test_Case.txt") and to also specify the desired output file name -
    # Only one file can be inputed at a time within the configuration
    file = input('Please Enter The File You Wish To Search For Prefix Notation: ')
    file_out = input('Please Enter The Name Of The Output File You Wish To Save In Folder: ')

    #while a given file ("Required Input.txt" or "Test_Case.txt") is open, search through each line of the prefix notation
    with open(file, 'r') as file:
        for line in file:
            # extract new line from given file
            line = line.strip()

            #if there are any blank lines within .txt file, ignore them
            if line == '':
                continue

            #dispaly/print the prefix code for each prefix notation for easy comparison with postfix - to "echo" the input
            with open(file_out, 'a') as path:
                print('Prefix Notation:', line,file=path)
            print('Prefix Notation:', line)

            #call reverse prefix notation funtion to reverse prefix string characters
            line = reverse(line)

            #convert prefix notation to postfix
            if prefix_to_postfix(line) == False:
                #print space between each postfix and prefix line item for easier interpretability
                with open(file_out, 'a') as path:
                    print(' ', file=path)
                print(' ')
                continue

