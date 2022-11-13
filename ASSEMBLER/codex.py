#converts the parsed asm data into binary code

comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
    }
    
def dest_comp_jump_splitter(instruction):
    d={"dest":"empty","comp":"empty","jump":"empty"}
    part = ""
    if not "=" in instruction:
        instruction = "empty=" + instruction
    if not ";" in instruction:
        instruction = instruction + ";empty"
    for i in instruction:
        if i == "=":
            d["dest"] = part
            part = ""
            continue
        if i == ";":
            d["comp"] = part
            part = ""
            continue
        part = part + i
    d["jump"] = part
    return d

def dest_binary_converter(data):
    d1,d2,d3=0,0,0
    if "A" in data:
        d1 = 1
    if "D" in data:
        d2 = 1
    if "M" in data:
        d3 = 1
    return str(d1)+str(d2)+str(d3)

def jump_binary_converter(data):
    j1,j2,j3=0,0,0
    if data == "JGT":
        j1,j2,j3=0,0,1
    elif data == "JEQ":
        j1,j2,j3=0,1,0
    elif data == "JGE":
        j1,j2,j3=0,1,1
    elif data == "JLT":
        j1,j2,j3=1,0,0
    elif data == "JNE":
        j1,j2,j3=1,0,1
    elif data == "JLE":
        j1,j2,j3=1,1,0
    elif data == "JMP":
        j1,j2,j3=1,1,1
    return str(j1)+str(j2)+str(j3)

def comp_binary_converter(data):
    return comp[str(data)]
    
def A_instruction_conversion(instruction):
    binary_val = "0" + str(bin(instruction).replace("0b", "").zfill(15))
    return binary_val

def C_instruction_conversion(instruction):
    binary_starter = "111"
    dic = dest_comp_jump_splitter(instruction)
    dest_binary = dest_binary_converter(dic["dest"])
    jump_binary = jump_binary_converter(dic["jump"])
    comp_binary = comp_binary_converter(dic["comp"])
    return binary_starter + comp_binary + dest_binary + jump_binary 
    
def main(data):
    forward_data = []
    for instruction in data:
        binary_instruction = ""
        if instruction[0] == "@":
            binary_instruction = A_instruction_conversion(int(instruction[1:]))
        else:
            binary_instruction = C_instruction_conversion(instruction)
        forward_data.append(binary_instruction)
    return forward_data

