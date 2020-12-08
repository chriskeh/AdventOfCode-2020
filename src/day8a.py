#!/usr/bin/env /usr/bin/python36

input_data_file = "day8.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Two lists.  One list contains the instructions, the second list contains the operands.
    """
    my_instructions = []
    my_operands = []

    with open(input_file, 'r') as f:
        i = 0
        for line in f:
            line = line.strip()
            inst, oper = line.split(" ")
            my_instructions.append(inst)
            my_operands.append(int(oper))
            i += 1

    return my_instructions, my_operands


def run_program(instruction, operand):
    """
    Execute the program which is given by two lists: one with the commands, the second with the operands.
    :param instruction: list with instructions
    :param operand: list with operands
    :return: 1) the outcome: True if the given program is infinite, False if it terminates
             2) the result in the accumulator
    """

    # Create a third list, its elements are False if this instruction has not been executed and will be set to True
    # once it is executed.
    execution = [False for i in range(0, len(instruction))]

    accumulator = 0
    instruction_counter = 0     # Keep track on which line of the program we are
    while True:
        if instruction_counter == len(instruction):
            # Reached end of instructions, so program terminates
            # print("Yesss, program terminates")
            unendlich = False
            break
        if execution[instruction_counter]:
            # We're executing a line a second time, so program is infinite
            # print("Program is infinite")
            unendlich = True
            break
        if instruction[instruction_counter] == "nop":
            execution[instruction_counter] = True
            instruction_counter += 1
            # print("NOP")
        elif instruction[instruction_counter] == "acc":
            execution[instruction_counter] = True
            accumulator += operand[instruction_counter]
            instruction_counter += 1
            # print("ACC, sum: {}".format(accumulator))
        elif instruction[instruction_counter] == "jmp":
            execution[instruction_counter] = True
            instruction_counter += operand[instruction_counter]
            # print("JMP: counter: {}".format(instruction_counter))
        else:
            exit("invalid instruction {}".format(instruction[instruction_counter]))

    return unendlich, accumulator


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "day8_test.data"

    all_instructions, all_operands = slurp_input(input_data_file)

    checked_line = 0                                  # a counter to track which line we're working on
    modified_instructions = all_instructions.copy()   # a copy of the original program, can be modified
    while checked_line < len(modified_instructions):
        # print("Line number: {}".format(checked_line))
        if modified_instructions[checked_line] == "acc":
            # print("Line {} acc".format(checked_line))
            checked_line += 1
            continue
        elif modified_instructions[checked_line] == "jmp":
            # print("Line {} jmp ==> nop".format(checked_line))
            modified_instructions[checked_line] = "nop"
        elif modified_instructions[checked_line] == "nop":
            # print("Line {} nop ==> jmp".format(checked_line))
            modified_instructions[checked_line] = "jmp"

        infinite, result = run_program(modified_instructions, all_operands)
        if not infinite:
            # That means the modified program teminated clean. So we can end here.
            break

        # Prepare next iteration in the while loop: create a fresh copy of the original and increase the line to inspect
        modified_instructions = all_instructions.copy()
        checked_line += 1

    if infinite:
        print("Unendlich: acc = {}".format(result))
    else:
        print("Sauber beendet: acc = {}".format(result))

    # print(checked_line)


if __name__ == "__main__":
    main()
