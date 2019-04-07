#################################################################################################################################
#Contains the necessary functions for the Sudoku Solver. The algorithms for simple number elimination are listed first, then    #
#supporting functions, and then the graph method.                                                                               #
#                                                                                                                               #
#################################################################################################################################


################Check for single values#################

def RowCheck(numbered, possibilities, notNumbers):
    for i in range(15,169,14):
        for j in range(i,i+11):
            for k in possibilities[j]:
                solution = 1
                for m in range(i,i+11):
                    if not m in notNumbers and k in possibilities[m] and not m == j:
                        solution = 0
                if solution == 1:
                    if type(k) == int:
                        possibilities[j] = [k]
                    else:
                        possibilities[j] = k
    return possibilities

def ColCheck(numbered, possibilities, notNumbers):
    for i in range(15,26):
        for j in range(i,169,14):
            for k in possibilities[j]:
                solution = 1
                for m in range(i,169,14):
                    if not m in notNumbers and k in possibilities[m] and not m == j:
                        solution = 0
                if solution == 1:
                    if type(k) == int:
                        possibilities[j] = [k]
                    else:
                        possibilities[j] = k
    return possibilities

def BoxCheck(numbered, possibilities):
    i = 15
    counter = 0
    while i < 136:
        counter += 1
        for j in range(i,i+29,14):
            for k in range(j,j+3):
                for m in possibilities[k]:
                    solution = 1
                    for n in range(i,i+29,14):
                        for x in range(n,n+3):
                            if m in possibilities[x] and not x == k:
                                solution = 0
                    if solution == 1:
                        if type(m) == int:
                            possibilities[k] = [m]
                        else:
                            possibilities[k] = m
        if counter == 3:
            counter = 0
            i += 48
        else:
            i += 4
    return possibilities

################"Cross out" values######################

def RowCross(numbered, allNum, possibilities):
    for i in range(0,169,14):
        for j in range(i,i+12):
            if numbered[j] in allNum:
                for k in range(i,i+12):
                    if not j == k and numbered[j] in possibilities[k]:
                        temp = possibilities[k][:]
                        temp.remove(numbered[j])
                        if type(temp) == int:
                            possibilities[k] = [temp[:]]
                        else:
                            possibilities[k] = temp[:]
    return possibilities

def ColCross(numbered, allNum, possibilities):
    for i in range(12):
        for j in range(i,i+169,14):
            if numbered[j] in allNum:
                for k in range(i,i+169,14):
                    if not j == k and numbered[j] in possibilities[k]:
                        temp = possibilities[k][:]
                        temp.remove(numbered[j])
                        if type(temp) == int:
                            possibilities[k] = [temp[:]]
                        else:
                            possibilities[k] = temp[:]
    return possibilities

def BoxCross(numbered, allNum, possibilities):
    i = 15
    counter = 0
    while i < 136:
        counter += 1
        for j in range(i,i+29,14):
            for k in range(j,j+3):
                if numbered[k] in allNum:
                    for m in range(i,i+29,14):
                        for n in range(m,m+3):
                            if not k == n and numbered[k] in possibilities[n]:
                                temp = possibilities[n][:]
                                temp.remove(numbered[k])
                                if type(temp) == int:
                                    possibilities[n] = [temp[:]]
                                else:
                                    possibilities[n] = temp[:]
        if counter == 3:
            counter = 0
            i += 48
        else:
            i += 4
    return possibilities

def PositionSolutions(numbered, puzzle, allNum, possibilities, notNumbers):
    for i in range(181):
        if not i in notNumbers and numbered[i] == 32:
            if len(possibilities[i]) == 1:
                numbered[i] = possibilities[i][0]
                puzzle = puzzle[:i] + str(chr(possibilities[i][0])) + puzzle[i+1:]
    return numbered, puzzle

def CheckErrors(numbered, puzzle, notNumbers, possibilities):
    for i in range(15,169,14):
        tempValues = []
        for j in range(i,i+12):
            if not numbered[j] == 32 and not j in notNumbers:
                if numbered[j] in tempValues:
                    #print(puzzle, end = '\n\n')
                    #raise Exception('Duplicates in a row. Second one found at position {0}'.format(j))
                    return 1
                else:
                    tempValues.append(numbered[j])
    for i in range(12):
        tempValues = []
        for j in range(i,i+169,14):
            if not numbered[j] == 32 and not j in notNumbers:
                if numbered[j] in tempValues:
                    #print(puzzle, end = '\n\n')
                    #raise Exception('Duplicates in a column. Second one found at position {0}'.format(j))
                    return 1
                else:
                    tempValues.append(numbered[j])
    i = 15
    counter = 0
    while i < 136:
        counter += 1
        tempValues = []
        for j in range(i,i+29,14):
            for k in range(j,j+3):
                if not numbered[k] == 32 and not k in notNumbers:
                    if numbered[k] in tempValues:
                        #print(puzzle, end = '\n\n')
                        #raise Exception('Duplicates in a box. Second one found at position {0}'.format(k))
                        return 1
                    else:
                        tempValues.append(numbered[k])
        if counter == 3:
            counter = 0
            i += 48
        else:
            i += 4
    for i in range(15,181):
        if i not in notNumbers and len(possibilities[i]) == 0:
            #raise Exception('Position {0} does not have any possibilities left'.format(i))
            return 1

    return 0

def RunCheck(numbered, puzzle, allNum, possibilities, notNumbers):
    error = 0
    possibilities = RowCheck(numbered, possibilities, notNumbers)
    possibilities = ColCheck(numbered, possibilities, notNumbers)
    possibilities = BoxCheck(numbered, possibilities)
    possibilities = RowCross(numbered, allNum, possibilities)
    possibilities = ColCross(numbered, allNum, possibilities)
    possibilities = BoxCross(numbered, allNum, possibilities)
    numbered, puzzle = PositionSolutions(numbered, puzzle, allNum, possibilities, notNumbers)
    error = CheckErrors(numbered, puzzle, notNumbers, possibilities)
    return possibilities, numbered, puzzle, error

def CheckSolution(notNumbers, numbered):
    solution = 1
    for i in range(181):
        if not i in notNumbers:
            if numbered[i] == 32:
                solution = 0
    return solution


def MakeGuess(numbered, puzzle, possibilities, allNum, notNumbers):     #Makes the first guess of a tree
    savedState = []
    savedPuzzle = puzzle
    savedPossibilities = []
    guess = []
    solutionFound = 0
    tempBadGuessCounter = 0

    for i in range(len(numbered)):                                                      #first runthrough, only guesses if theres a 50% chance of correctness
        if i not in notNumbers and len(possibilities[i]) == 2:
            for j in range(len(possibilities[i])):
                savedState = numbered[:]
                guess = [i,j]
                savedPossibilities = possibilities[:]
                possibilities[i] = [possibilities[i][j]]
                badGuess = 0
                tempPossibilities = []
                while not badGuess and not tempPossibilities == possibilities:
                    tempPossibilities = possibilities[:]
                    possibilities, numbered, puzzle, badGuess = RunCheck(numbered, puzzle, allNum, possibilities, notNumbers)
                    print(puzzle, end = '\n\n')
                    if CheckSolution(notNumbers, numbered):
                        return 1, numbered, puzzle, possibilities
                tempBadGuessCounter += 1
                numbered = savedState[:]
                puzzle = savedPuzzle
                possibilities = savedPossibilities[:]

    for i in range(len(numbered)):                                                      #second runthrough, assumes a more complex puzzle
        if i not in notNumbers and len(possibilities[i]) > 1:
            for j in range(len(possibilities[i])):
                savedState = numbered[:]
                guess = [i,j]
                savedPossibilities = possibilities[:]
                possibilities[i] = [possibilities[i][j]]
                badGuess = 0
                tempPossibilities = []
                while not badGuess and not tempPossibilities == possibilities:
                    tempPossibilities = possibilities[:]
                    possibilities, numbered, puzzle, badGuess = RunCheck(numbered, puzzle, allNum, possibilities, notNumbers)
                    print(puzzle, end = '\n\n')
                    if CheckSolution(notNumbers, numbered):
                        return 1, numbered, puzzle, possibilities
                if not badGuess:
                    solutionFound, numbered, puzzle, possibilities = MakeGuessLowest(numbered, puzzle, possibilities, allNum, notNumbers)
                    if solutionFound == 1:
                        return 1, numbered, puzzle, possibilities
                tempBadGuessCounter += 1
                numbered = savedState[:]
                puzzle = savedPuzzle
                possibilities = savedPossibilities[:]

    return

def MakeGuessLowest(numbered, puzzle, possibilities, allNum, notNumbers):   #Makes the last possible guess of a tree
    savedState = []
    savedPuzzle = puzzle
    savedPossibilities = []
    guess = []
    solutionFound = 0
    tempBadGuessCounter = 0

    for i in range(len(numbered)):
        if i not in notNumbers and len(possibilities[i]) == 2:
            for j in range(len(possibilities[i])):
                savedState = numbered[:]
                guess = [i,j]
                savedPossibilities = possibilities[:]
                possibilities[i] = [possibilities[i][j]]
                badGuess = 0
                tempPossibilities = []
                while not badGuess and not tempPossibilities == possibilities:
                    tempPossibilities = possibilities[:]
                    possibilities, numbered, puzzle, badGuess = RunCheck(numbered, puzzle, allNum, possibilities, notNumbers)
                    print(puzzle, end = '\n\n')
                    if CheckSolution(notNumbers, numbered):
                        return 1, numbered, puzzle, possibilities
                tempBadGuessCounter += 1
                numbered = savedState[:]
                puzzle = savedPuzzle
                possibilities = savedPossibilities[:]
        if i not in notNumbers and len(possibilities[i]) > 1:
            for j in range(len(possibilities[i])):
                savedState = numbered[:]
                guess = [i,j]
                savedPossibilities = possibilities[:]
                possibilities[i] = [possibilities[i][j]]
                badGuess = 0
                tempPossibilities = []
                while not badGuess and not tempPossibilities == possibilities:
                    tempPossibilities = possibilities[:]
                    possibilities, numbered, puzzle, badGuess = RunCheck(numbered, puzzle, allNum, possibilities, notNumbers)
                    print(puzzle, end = '\n\n')
                    if CheckSolution(notNumbers, numbered):
                        return 1, numbered, puzzle, possibilities
                tempBadGuessCounter += 1
                numbered = savedState[:]
                puzzle = savedPuzzle
                possibilities = savedPossibilities[:]

    return 0, numbered, puzzle, possibilities












    #solutionFound = MakeGuess(numbered, puzzle, possibilities, allNum, notNumbers)
    #return solutionFound




###backup###
#def MakeGuess(numbered, puzzle, possibilities, allNum, notNumbers):     #does not yet account for recursive guesses
#    savedState = []
#    savedPuzzle = puzzle
#    savedPossibilities = []
#    guess = []
#    solutionFound = 0
#    tempBadGuessCounter = 0

#    for i in range(len(numbered)):
#        if i not in notNumbers and len(possibilities[i]) > 1:
#            for j in range(len(possibilities[i])):
#                savedState = numbered[:]
#                guess = [i,j]
#                savedPossibilities = possibilities[:]
#                possibilities[i] = [possibilities[i][j]]
#                badGuess = 0
#                tempPossibilities = []
#                while not badGuess and not tempPossibilities == possibilities:
#                    tempPossibilities = possibilities[:]
#                    possibilities, numbered, puzzle, badGuess = RunCheck(numbered, puzzle, allNum, possibilities, notNumbers)
#                    print(puzzle, end = '\n\n')
#                    if CheckSolution(notNumbers, numbered):
#                        return 1, numbered, puzzle, possibilities
#                tempBadGuessCounter += 1
#                numbered = savedState[:]
#                puzzle = savedPuzzle
#                possibilities = savedPossibilities[:]        # []?

#    raise Exception('No solution found')
#    #solutionFound = MakeGuess(numbered, puzzle, possibilities, allNum, notNumbers)
#    #return solutionFound