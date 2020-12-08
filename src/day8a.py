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


def main():

    # read the input data
    input_data_file = "day8_test.data"

    all_instructions, all_operands = slurp_input(input_data_file)
    # print(all_instructions)
    # print(all_operands)

    # Create a third list that holds the number of executions of the command in each line. Initially 0
    # Could be improved with True and False ?!?
    execution = [False for i in range(0, len(all_instructions))]

    accumulator = 0

    # result = run_program(all_instructions, all_operands)
    instruction_counter = 0
    while True:
        if instruction_counter == len(all_instructions):
            print("Yesss, program terminates")
            break
        if execution[instruction_counter]:
            print("Exiting the loop")
            break
        if all_instructions[instruction_counter] == "nop":
            execution[instruction_counter] = True
            instruction_counter += 1
            print("NOP")
        elif all_instructions[instruction_counter] == "acc":
            execution[instruction_counter] = True
            accumulator += all_operands[instruction_counter]
            instruction_counter += 1
            print("ACC, sum: {}".format(accumulator))
        elif all_instructions[instruction_counter] == "jmp":
            execution[instruction_counter] = True
            instruction_counter += all_operands[instruction_counter]
            print("JMP: counter: {}".format(instruction_counter))
        else:
            exit("invalid instruction {}".format(all_instructions[instruction_counter]))

    print("Accumulator: {}".format(accumulator))
    # print(len(all_instructions), len(all_operands), len(execution))

    # print("Total: {}".format(total))

if __name__ == "__main__":
    main()
