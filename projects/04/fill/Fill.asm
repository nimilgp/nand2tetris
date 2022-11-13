// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
@color
M=0

@8192
D=A

@n
M=D

(CHECKLOOP)
@KBD
D=M
@BLACK
D;JGT
@WHITE
D;JEQ

(BLACK)
D=-1
@colour
M=D
@FILLIN
0;JMP

(WHITE)
@colour
M=0
@FILLIN
0;JMP

(FILLIN)
@i
M=1
@SCREEN
D=A
@addr
M=D

(LOOP)
@i
D=M
@n
D=D-M
@CHECKLOOP
D;JGT
@colour
D=M
@addr
A=M
M=D

@i
M=M+1
@addr
M=M+1
@LOOP
0;JMP