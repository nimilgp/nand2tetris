// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
@R2
M=0 //clear R2

@R0
D=M
@ZEROCONDITION
D;JEQ

@R1
D=M
@ZEROCONDITION
D;JEQ

@i 
M=0 //i=0

(LOOP)
@i
D=M
@R1
D=D-M
@END
D;JEQ //if i=n goto END

@R2
D=M
@R0
D=D+M //add to R2
@R2
M=D
@i
M=M+1
@LOOP
0;JMP

(ZEROCONDITION) //if R0 or R1 is zero
@R2
M=0

(END)
@END
0;JMP

