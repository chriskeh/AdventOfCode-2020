#!/usr/bin/env /usr/bin/python36

input_data_file = "day8.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Two lists.  One list contains the instructions, the second list contains the operands.
    """
    my_instructions = []
    my_operands =[]

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
    :return: the result in the accumulator
    """

    # Create a third list that holds the number of executions of the command in each line. Initially 0
    # Could be improved with True and False ?!?
    execution = [False for i in range(0, len(instruction))]

    accumulator = 0
    instruction_counter = 0
    while True:
        if instruction_counter == len(instruction):
            print("Yesss, program terminates")
            break
        if execution[instruction_counter]:
            print("Exiting the loop")
            break
        if instruction[instruction_counter] == "nop":
            execution[instruction_counter] = True
            instruction_counter += 1
            print("NOP")
        elif instruction[instruction_counter] == "acc":
            execution[instruction_counter] = True
            accumulator += operand[instruction_counter]
            instruction_counter += 1
            print("ACC, sum: {}".format(accumulator))
        elif instruction[instruction_counter] == "jmp":
            execution[instruction_counter] = True
            instruction_counter += operand[instruction_counter]
            print("JMP: counter: {}".format(instruction_counter))
        else:
            exit("invalid instruction {}".format(instruction[instruction_counter]))

    return(accumulator)


def main():

    # read the input data
    input_data_file = "day8_test.data"

    all_instructions, all_operands = slurp_input(input_data_file)
    # print(all_instructions)
    # print(all_operands)


    result = run_program(all_instructions, all_operands)

    print("Accumulator: {}".format(result))
    # print(len(all_instructions), len(all_operands), len(execution))

    # print("Total: {}".format(total))

if __name__ == "__main__":
    main()
