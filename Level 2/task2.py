#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_string():
    global input_sequence
    input_sequence = raw_input("Enter a sequence which first occurance "
    "index you want to find \n(it should be an integer with 0-9 characters): ")
    if str(input_sequence).isdigit() == False:
        print("Sequence may contain only 0-9 characters! ")
        return False
    return True

def search(input_sequence):
    input_string = list(str(input_sequence))
    infinite_sequence = ['1']
    next_step_number = 1
    find_status = False
    while find_status == False:
        input_string_index = 0
        lenght = len(input_string)
        for sequence_digit in infinite_sequence:
            next_step_number += 1
            infinite_sequence += (list(str(next_step_number)))
            if  sequence_digit == input_string[input_string_index]:
                input_string_index += 1
            else:
                input_string_index = 0
            if input_string_index == lenght:
                find_status = True
                return next_step_number - lenght
def printer(result):
    print("First occurrence at index {}.").format(result)

def main():
    if get_string() == True:
        result = search(input_sequence)
        printer(result)

if __name__ == "__main__":
    main()
