import heapq
import time
import math

from copy import deepcopy

def AStar(start, goal):
    heap = []
    parents = {}
    heuristics = {} #heuristic
    gScores = {} #shortest path to end

    gScores[start] = 0
    heuristics[start] = 0
    parents[start] = None
    heapq.heapify(heap)
    heapq.heappush(heap, (0,start))
    while len(heap) > 0:
        current = heapq.heappop(heap)
        if current[1] == goal:
            print (reconstructPath(current[1], start, parents))
            break
        pos = getPos(current)
        distance = gScores[current[1]]
        for states in pos:
            if states not in gScores or gScores[states] > distance + 1:
                gScores[states] = distance + 1
                if states not in heuristics:
                    heuristics[states] = manhattan(states)
                parents[states] = current[1]
                heapq.heappush(heap, (gScores[states] + heuristics[states], states))
def whatStep(current, parent):
  currentIndex = current.index(0)
  parentIndex = parent.index(0)
  toReturn = ""
  difference = parentIndex - currentIndex
  if difference == -4:
    toReturn = "U"
  elif difference == 4:
    toReturn ="D"
  elif difference == -1:
    toReturn = "L"
  elif difference == 1:
    toReturn = "R"
  else:
    toReturn = "n"
  return toReturn
def reconstructPath(current, start, parents):
    actualSteps = ""
    steps = 0
    while current != start:
        parent = parents[current]
        actualSteps = actualSteps + (whatStep(current, parent))
        steps = steps +1
        current = parent
    return steps, actualSteps[::-1] #reverse the output string
def swap(node, a, b):
    listTemp = list(node)
    temp = listTemp[a]
    listTemp[a] = listTemp[b]
    listTemp[b] = temp
    toReturn = tuple(listTemp)
    return toReturn
def getPos(current):
    pos = []
    node = current[1]
    x = node.index(0)
    r = math.floor(x/4)
    c = x % 4
    if r < 3:
        newState = swap(node, x, x + 4)
        pos.append(newState)
    if r > 0:
        newState = swap(node, x, x - 4)
        pos.append(newState)
    if c > 0:
        newState = swap(node, x, x - 1)
        pos.append(newState)
    if c < 3:
        newState = swap(node, x, x + 1)
        pos.append(newState)
    return pos
def manhattan(state):
    heuristic = 0
    for element in range(0, 16):
        value = state[element]
        if value != 0:
            originalY = (element) % 4
            originalX = (element) / 4
            targetY = (value - 1) % 4
            targetX = (value - 1) / 4
            Ychange = (originalY - targetY)
            Xchange = (originalX - targetX)
            heuristic = heuristic + abs(Ychange) + abs(Xchange)
    return heuristic



puzzleNumber = input("What number puzzle do you want to solve? ")
puzzleList = []
puzzleFile = open("Puzzle" + str(puzzleNumber) + ".txt", 'r')
puzzleString = puzzleFile.read()
for number in puzzleString.split():
    puzzleList.append(int(number))
start = time.time()
puzzle = tuple(puzzleList)
goalState = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
AStar(puzzle, goalState)
print (time.time() - start)