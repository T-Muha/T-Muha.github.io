#################################################################################################################################
#Solves Sudoku puzzles through both an algorithm and a graph. If the algorithm reaches a dead end, the algorithm and graph are  #
#then used interchangeably. Can currently solve puzzles with at most one level of guessing necessary.                           #
#                                                                                                                               #
#################################################################################################################################

from MultiLevelFunctions import *
import time, random, json
from flask import Flask, render_template, request, redirect, Response
import json

app = Flask(__name__)
@app.route("/")
def output():
	return render_template("SodokuSolverPage.html", name="Joe")

# @app.route("/receiver", methods = ["POST"])
# def worker():
#     data = request.get_json()
#     print(data)
#     result = ""
#     for item in data:
#         result += str(item["make"]) + "\n"
#     return result

if __name__ == "__main__":
    app.run()

#lvlCharCounter = 97

#for ii in range(1,16):
#    for jj in range(3):
#        if ii > 9:
#            tempString = 's' + str(ii) + str(chr(lvlCharCounter + jj)) + '.txt'
#            puzzleFile = open(tempString, 'r')
#        else:
#            tempString = 's' + '0' + str(ii) + str(chr(lvlCharCounter + jj)) + '.txt'
#            puzzleFile = open(tempString, 'r')
#        puzzle = puzzleFile.read()
#        numbered = [ord(i) for i in puzzle]
#        print(tempString)

#        allNum = [49,50,51,52,53,54,55,56,57]
#        possibilities = [allNum[:]] * 182
#        asciiNumCode = ['1','2','3','4','5','6','7','8','9']
#        notNumbers = []

#        for i in range(181):
#            if numbered[i] == 35:
#                notNumbers.append(i)
#            elif not numbered[i] == 32:
#                possibilities[i] = [numbered[i]]

#        print(puzzle, end = '\n\n')

#        tempPossibilities = []
#        error = 0
#        solutionFound = 0
#        counter = 0

#        while not CheckSolution(notNumbers, numbered) and not solutionFound:
#            tempPossibilities = possibilities[:]
#            possibilities, numbered, puzzle, error = RunCheck(numbered, puzzle, allNum, possibilities, notNumbers)
#            if error == 1:
#                raise Exception('Mistake found in puzzle. Ending program execution')
#            print(puzzle, end = '\n\n')
#            if CheckSolution(notNumbers, numbered):                                                                                   #not all solution checks may be necessary
#                print('solution found')
#            elif tempPossibilities == possibilities:
#                solutionFound, numbered, puzzle, possibilities = MakeGuess(numbered, puzzle, possibilities, allNum, notNumbers)
#        if CheckErrors(numbered, puzzle, notNumbers, possibilities) == 1:
#            print(puzzle, end = '\n\n')
#            raise Exception('Mistake made. File is s{0}'.format(ii))
















puzzleFile = open('HardestPuzzle.txt', 'r')
puzzle = puzzleFile.read()
numbered = [ord(i) for i in puzzle]

allNum = [49,50,51,52,53,54,55,56,57]
possibilities = [allNum[:]] * 182
asciiNumCode = ['1','2','3','4','5','6','7','8','9']
notNumbers = []

for i in range(181):
    if numbered[i] == 35:
        notNumbers.append(i)
    elif not numbered[i] == 32:
        possibilities[i] = [numbered[i]]

print(puzzle, end = '\n\n')

tempPossibilities = []
error = 0
solutionFound = 0
counter = 0

while not CheckSolution(notNumbers, numbered) and not solutionFound:
    tempPossibilities = possibilities[:]
    possibilities, numbered, puzzle, error = RunCheck(numbered, puzzle, allNum, possibilities, notNumbers)
    if error == 1:
        raise Exception('Mistake found in puzzle. Ending program execution')
    print(puzzle, end = '\n\n')
    if CheckSolution(notNumbers, numbered):                                                                                   #not all solution checks may be necessary
        print('solution found')
    elif tempPossibilities == possibilities:
        solutionFound, numbered, puzzle, possibilities = MakeGuess(numbered, puzzle, possibilities, allNum, notNumbers)
if CheckErrors(numbered, puzzle, notNumbers, possibilities) == 1:
    print(puzzle, end = '\n\n')
    raise Exception('Mistake made. File is s{0}'.format(i))