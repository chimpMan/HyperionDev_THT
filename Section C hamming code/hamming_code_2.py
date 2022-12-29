import numpy as np


def hamming_checker(block):

    # Stores the binary form of the error bit
    parity_array = []

    # List comprehension to split the block into a list of strings
    string_split = [num for num in block]

    # Converting the list of strings to a list of integers
    digits = [int(i) for i in string_split]

    # Creating a 4x4 array using the list of integers
    binary_digits = np.array(digits).reshape(4, 4)

    # Slicing and storing 4 regions of our hamming code
    r1 = binary_digits[:, 1::2]
    r2 = binary_digits[:, 2:]
    r4 = binary_digits[1::2, :]
    r8 = binary_digits[2:4]

    # Summing up the bits in each region
    r1_count = r1.sum()
    r2_count = r2.sum()
    r4_count = r4.sum()
    r8_count = r8.sum()

    # Function that checks the parity of indivdual regions
    def parity_check():
        if(r8_count % 2 != 0):
            parity_array.append(1)
        else:
            parity_array.append(0)
        if(r4_count % 2 != 0):
            parity_array.append(1)
        else:
            parity_array.append(0)
        if(r2_count % 2 != 0):
            parity_array.append(1)
        else:
            parity_array.append(0)
        if(r1_count % 2 != 0):
            parity_array.append(1)
        else:
            parity_array.append(0)

        return(parity_array)

    # Function to find the error bit
    def error_bit(parity_arr=[]):
        error_string = [str(i) for i in parity_arr]
        bits = int("".join(error_string), 2)
        return bits

    # Function that returns the corrected original message
    def message_array():
        final = ''
        change = ''
        error_position = error_bit(parity_array)
        original = digits

        if (error_position != 0):
            if (original[error_position] == 1):
                original[error_position] = 0
                change = f'The corrupted bit was bit {error_bit(parity_array)} changed from 1 to 0'
            else:
                original[error_position] = 1
                change = f'The corrupted bit was bit {error_bit(parity_array)} changed from 0 to 1'
        else:
            original = digits
            change = 'there is no error'

        string_original = "".join(str(y) for y in original)
        final = f'hamming_checker({block}) -> {string_original} {change}'
        print(final)

        return string_original

    # Calling parity check to populate parity array
    parity_check()

    # Calling error bit to obtain the error bit
    error_bit(parity_array)
    
    # returning the message
    return message_array()


def main():

    # Loop the execution until the proper input is given
    # Input is given as an integer that is cast to String
    # ValueError is raised should the input be wrong
    while True:
        user_input = (input('enter a 16 bit binary digit: '))
        try:

            # A set is used to check the base of the input
            set_bin = {'0', '1'}
            set_ui = set(user_input)

            if (len((user_input)) == 16 and (set_bin == set_ui or set_ui == {'0'} or set_ui == {'1'})):
                hamming_checker(user_input)

            else:
                print('only 16 binary bits are acceptable')
                raise ValueError

            break

        except ValueError:
            print('Invalid Input. Try again.')

main()
