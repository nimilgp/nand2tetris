#writes the assemble for these commands
import commandflowcontrol

arithmetic_command_asm ={
"add":
"""@SP
AM=M-1
D=M
A=A-1
M=D+M""",

"sub":
"""@SP
AM=M-1
D=M
A=A-1
M=M-D""",

"neg":
"""@SP
A=M-1
M=-M""",

"eq":
"""@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@EQ_labelcount
D;JEQ
@SP
A=M-1
M=0
(EQ_labelcount)""",

"gt":
"""@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@GT_labelcount
D;JGT
@SP
A=M-1
M=0
(GT_labelcount)""",

"lt":
"""@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@LT_labelcount
D;JLT
@SP
A=M-1
M=0
(LT_labelcount)""",

"and":
"""@SP
AM=M-1
D=M
A=A-1
M=D&M""",

"or":
"""@SP
AM=M-1
D=M
A=A-1
M=D|M""",

"not":
"""@SP
A=M-1
M=!M"""}

segment_dict ={
    "local":"LCL",
    "argument":"ARG",
    "this":"THIS",
    "that":"THAT"}

def end():
    return """(END)
@END
0;JMP"""

def writearithmetic(command):
    return arithmetic_command_asm[command]

def returnsegment_dict(code):
    return segment_dict[code]

def writepushpop(pushpop,val,segment):
    if pushpop == "C_PUSH" and segment == "constant":
        return """@{}
D=A
@SP
A=M
M=D
@SP
M=M+1""".format(val)
    
    elif pushpop == "C_PUSH" and segment in ("local","argument","this","that"):
        baseaddr = returnsegment_dict(segment)
        return """@{}
D=M
@{}
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1""".format(baseaddr,val)
    
    elif pushpop == "C_POP" and segment in ("local","argument","this","that"):
        baseaddr = returnsegment_dict(segment)
        return """@{}
D=M
@{}
D=D+A
@R13
M=D
@SP
AM=M-2
D=M
@R13
A=M
M=D""".format(baseaddr,val)

def main(parsedlist):
    labelcount = 0
    asmlist = []
    for line in parsedlist:
        command_type = commandflowcontrol.command_type(line)
        if command_type == "C_ARITHMETIC":
            tempwrite = writearithmetic(line[0])
            write = tempwrite.replace("_labelcount",str(labelcount))
            asmlist.append(write)
            labelcount += 1
        elif command_type in ("C_PUSH","C_POP"):
            val = line[2]
            segment = line[1]
            write = writepushpop(command_type,val,segment)
            asmlist.append(write)
    write = end()
    asmlist.append(write)
    return asmlist
        
        
