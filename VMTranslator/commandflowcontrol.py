#command flow control

command_dict ={
    #arithmetic
    "add":"C_ARITHMETIC",
    "sub":"C_ARITHMETIC",
    "neg":"C_ARITHMETIC",
    "eq":"C_ARITHMETIC",
    "gt":"C_ARITHMETIC",
    "lt":"C_ARITHMETIC",
    "and":"C_ARITHMETIC",
    "or":"C_ARITHMETIC",
    "not":"C_ARITHMETIC",
    #branching
    "label":"C_LABEL",
    "goto":"C_GOTO",
    "if-goto":"C_IF",
    #function-
    "function":"C_FUNCTION",
    "call":"C_CALL",
    "return":"C_RETURN",
    #memory access commands
    "pop":"C_POP",
    "push":"C_PUSH"
    }

def command_type(commandline):#returns command type
    command_type = command_dict[commandline[0]]
    return command_type

"""
def arg1(commandline):#returns arg1
    command = command_type(commandline)
    if command == "C_ARITHMETIC":
        return commandline[0]
    elif command != "C_RETURN":
        return commandline[1]

def arg2(commandline):#return arg2
        return commandline[2]
"""
