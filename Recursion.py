"""
Data Structures, Lab 2 - (prefix to postfix conversion) utilizing a recursive function - Sam Dreyfuss
Reference for some coding structure: Problem Solving with Algorithms and Data Structures, Miller and Ranum

The algorithm below allows the user to type in a specified .txt file name they would like to convert from prefix to postfix
notation. The recursive_prefix_to_postfix algorithm is called which completes the conversion (more details on the
recursive_prefix_to_postfix algorithm below). The postfix output is saved down to the output file which is also specified by
the user.
"""

def recursive_prefix_to_postfix(data):
    '''The recursive_prefix_to_postfix algorithm will convert prefix to postfix notation utilizing a recursive structure instead of
    an iterative structure. Upon the first call the prefix notation data string will be read into the algorithm. The algorithm will
    recognize the 'acceptable' operator values: ['+', '-', '*', '/', '$']. The algorithm will then confirm if the next character is
    either an operator or operand. If a nonaccepable character is recognized the algorithm will generate an error. If the approriate
    sequence of either operand or operator is recognized the algorithm will begin to group the operand and operators
    in an operand + operand + operator format then proceed to the next portion of the prefix notation. The algorithm will
    continue to recursively scan the prefix notation until the base case is met and the algorithm is finished running.
    This will allow the user to convert for example an '+-abc' (prefix notaion) to an 'ab+c-' (postfix notation) by
    utilizing recursion.
    '''

    #define operators
    operators = ['+', '-', '*', '/', '$']

    #basecase for recursive algorithm structure. Finish method if prcessing data is less than 1 character in lengh
    #return blank tuple if base case is reached
    if len(data) < 1:
        return('','')

    #define "next" as first item in prefix notation string data
    next = data[0]

    #look to current data value in prefix expression within string, recognize operator values and confirm if the next value
    #is either operator or operand. If the appropriate charcters are recognized then create a operand + operand + operator
    #structure. If incorrect charactor is recognized - generate and error. Continue to call the function until the
    #basecase is met
    if next in operators:
        operator = next
        (bool ,operand_1, data) = recursive_prefix_to_postfix(data[1:])
        if len(data) < 1:
            return False, 'Error: Prefix Expression Is Not Possible To Convert - Please Check Syntax', ''
        if bool == False:
            return False, operand_1, ''
        (bool, operand_2, data) = recursive_prefix_to_postfix(data)
        return True, operand_1 + operand_2 + operator, data
    else:
        #confirm prefix syntax only includes "valid" characters (including alpha and numeric characters).
        #if error is found, print message to file in addition to printing to terminal
        if (ord(next) not in range(65, 91) and (ord(next) not in range(97, 123))):
        # if error is found, print error message
                return False, 'Invalid Character Found - Please Check Data Input File Regarding Character.', ''
        return True, next, data[1:]


#define a single driver to execute code - let user know if code is "Running as Expected":
if __name__ == '__main__':
    print('Code Running As Expected')

    # ask user for input file name ("Required Input.txt" or "Test_Case.txt") and to also specify the desired output file name -
    # Only one file can be input at a time within the configuration
    file_in = input('Please Enter The File You Wish To Search For Prefix Notation: ')
    #error check to confirm the file is a .txt file format, if so display error in console
    if file_in[-4:] != '.txt':
        print(file_in[-4:])
        print('Incorrect File Input Name. Please Check File Name For Typos')

    # while a given file ("Required Input.txt" or "Test_Case.txt") is open, search through each line of the prefix notation
    file_out = input('Please Enter The Name Of The Output File You Wish To Save In Folder: ')
    #error check to confirm the file is a .txt file forma, if so display error in console and print incorrect file name out
    #output
    if file_out[-4:] != '.txt':
        print('Incorrect File Output Name. Please Check File Name For Typos')
        with open(file_out, 'a') as path:
            print('Incorrect File Output Name. Please Check File Name For Typos', file_out, file=path)

    #print name of input file to top of output file for each input file processed and to terminal
    with open(file_out, 'a') as path:
        print('Converting Prefix From File:', file_in, '\n',file=path)
        print('Converting Prefix From File:', file_in, '\n')

    #open input file and read into algorithm
    with open(file_in, 'r') as file_in:
        for line in file_in:
            # extract new line from given file
            line = line.strip()

            #if there are any blank lines within .txt file, ignore them
            if line == '':
                continue

            #dispaly/print the prefix code for each prefix notation for easy comparison with postfix - to "echo" the input
            with open(file_out, 'a') as path:
                print('Prefix Notation:', line,file=path)
            print('Prefix Notation:', line)

            # convert prefix notation to postfix
            with open(file_out, 'a') as path:
                # print space between each postfix and prefix line item for easier interpretability
                    postfix_notation = recursive_prefix_to_postfix(line)

                    #if no error was found in sytax, print postfix format to both termina and output file. If syntax error
                    #is found print to file and terminal
                    if not postfix_notation[0]:
                        print(postfix_notation[1], '\n')
                        print(postfix_notation[1] ,'\n',file=path)
                        #print()
                    else:
                        if len(line) != len(postfix_notation[1]):
                            print('Error: Prefix Expression Is Not Possible To Convert - Please Check Syntax','\n',file=path)
                            print('Error: Prefix Expression Is Not Possible To Convert - Please Check Syntax','\n')
                        else:
                            print('Postfix Notation:', postfix_notation[1], '\n',file=path)
                            print('Postfix Notation: ', postfix_notation[1], '\n')
                            continue
