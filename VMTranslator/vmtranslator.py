VM_file = "BasicTest.vm"  #vm input file name
ASM_file = "BasicTest.asm" #asm output file name

import parser
parsedlist = parser.main(VM_file)

import codewriter
asmlist = codewriter.main(parsedlist)

writefile = open(ASM_file,"w")
for i in range(len(asmlist)):
    writefile.write(asmlist[i])
    writefile.write("\n")
writefile.close()

