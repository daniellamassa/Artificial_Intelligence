from eightPuzzle import *

GOALSTATE = [1,2,3,8,' ',4,7,6,5]
STATES = ["State A","State B","State C","State D","State E","State F","State G","State H"]
STEP_COUNT = []
PUZZLES = [[' ',1,3,8,2,4,7,6,5],[1,3,4,8,6,2,' ',7,5],[1,3,' ',4,2,5,8,7,6],[7,1,2,8,' ',3,6,5,4],
            [8,1,2,7,' ',4,6,5,3],[2,6,3,4,' ',5,1,8,7],[7,3,4,6,1,5,8,' ',2],[7,4,5,6,' ',3,8,1,2]]

state_counter = 0
for item in PUZZLES:
    print(STATES[state_counter])
    print()
    InformedSearch(EightPuzzle(item), EightPuzzle(GOALSTATE), True)
    state_counter += 1

'''
counter = 0
for state in STATES:
    print(state + " Number of steps: " +str(STEP_COUNT[counter]))
    counter += 1
'''
