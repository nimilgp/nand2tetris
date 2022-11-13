ASM_file = "SimpleAdd.asm"  #asm input file name
HACK_file = "SimpleAdd.hack" #hack output file name

import parser
parsedlist = parser.main(ASM_file)

import preprocessor
preprocessedlist = preprocessor.main(parsedlist)

import codex
binarylist = codex.main(preprocessedlist)

writefile = open(HACK_file,"w")
for i in range(len(binarylist)):
    writefile.write(binarylist[i])
    writefile.write("\n")
writefile.close()
