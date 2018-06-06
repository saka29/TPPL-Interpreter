# TPPL-Interpreter
A Python interpreter for my TPPL Esoteric language (See https://esolangs.org/wiki/TPPL). The interpreter will be updated as the language is updated.
## What is TPPL?
TPPL is an esolang I made that's based around toilet paper. It is stack based but read like a tape as in only 1 value is "seen" as a time.<br>
Each TPPL program is written in all caps and starts with "ENTER BATHROOM" or "ENTER RESTROOM" for obvious reasons.<br>
Each program starts with a roll of fresh toilet paper with length 1, AKA a stack with 1 item with value 0.<br> 
Each sheet of toilet paper (Item in the stack) can have a value from 0 to 2 (Inclusive), this is because the toilet paper used is 2-ply.<br>
There are 3 places data may be stored, the main roll, the HOLD slot, and the trash bin. In the HOLD and trash bin, the values get converted into a sequence, represented as numbers separated by commas (e.g. 1,0,2,2).<br>
## Why program in TPPL?
There's really no reason to program in TPPL unless you want to have some fun hehe.
## Setup
You will need Python 3.5 (Or up? I haven't tested it with Python 3.6 but I'm pretty sure it should work.) and a command line that can run python.<br>
Simply download the from the master branch and do something like
```
cd C:/MyDirectory/Folders/MoreFolders/TPPL-Interpreter/main/
```
to go into the directory, and run it like the following:
```
interpreter.py myprogram.txt
```
replace myprogram.txt with the file you wish to run.
## Tutorial
Coming soon, for now see https://esolangs.org/wiki/TPPL
## Possible Future Additions
* Arithmetic
* Relative jumps
