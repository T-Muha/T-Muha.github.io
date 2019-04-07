#################################################################################################################################
#Takes levels downloaded from http://lipas.uwasa.fi/~timan/sudoku/ and converts its characters to characters used in            #
#SudokuSolver.py                                                                                                                #
#                                                                                                                               #
#################################################################################################################################

import os

for fileName in os.listdir('C:\\Users\\noy5eg\\Documents\\sudokus'):
    if fileName.endswith('.txt'):
        puzzleFile = open(fileName,'r')
        puzzle = puzzleFile.read()
        numbered = [ord(i) for i in puzzle]
        newPuzzle = []

        for i in range(13):
            newPuzzle.append(35)

        newPuzzle.append(10)
        newPuzzle.append(35)

        counter = 0
        newLineCounter = 1

        for i in range(len(numbered)-1):

            if i == len(numbered)-2:

                newPuzzle.append(35)
                newPuzzle.append(10)

                for i in range(13):
                    newPuzzle.append(35)

            elif numbered[i] == 10:

                if newLineCounter % 3 == 0:

                    newPuzzle.append(35)
                    newPuzzle.append(10)

                    for i in range(13):
                        newPuzzle.append(35)

                    newPuzzle.append(10)
                    newPuzzle.append(35)

                else:
                    newPuzzle.append(35)
                    newPuzzle.append(10)
                    newPuzzle.append(35)
                counter = 0
                newLineCounter += 1

            elif counter == 3 and not numbered[i] == 32:

                newPuzzle.append(35)

                if numbered[i] == 48:
                    newPuzzle.append(32)
                else:
                    newPuzzle.append(numbered[i])
                counter = 1

            elif numbered[i] == 48:

                newPuzzle.append(32)
                counter += 1

            elif not numbered[i] == 32:

                newPuzzle.append(numbered[i])
                counter += 1


        newString = ''
        for i in newPuzzle:
            newString = newString + str(chr(i))


        print(newString)

        puzzleFile.close()
        puzzleFile = open(fileName,'w')

        puzzleFile.write(newString)

        puzzleFile.close()