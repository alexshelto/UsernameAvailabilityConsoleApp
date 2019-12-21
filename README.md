# UsernameAvailabilityConsoleApp

## How it works
* Program will take a textfile of usernames or generate custom usernames
* Checks Twitter & Instagram for username availability and writes a textfile of names to use

## Running the code
Python main.py {twitter OR instagram} {optional, textfile name}
* ex.1: python main.py twitter checkNames.txt // will search names from text file
* ex.2: python main.py twitter                // will generate custom usernames of a given length to search

## Notice
If you generate custom usernames it will attempt all permutations of a given set of letters to a length n
program takes roughly .42 secconds per username check so keep time in mind
