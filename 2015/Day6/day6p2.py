import numpy as np
import re
import cv2

def turnOn(grid, corner1, corner2):
    grid[corner1[1]:corner2[1]+1, corner1[0]:corner2[0]+1] += 1
    return grid

def toggle(grid, corner1, corner2):
    grid[corner1[1]:corner2[1]+1, corner1[0]:corner2[0]+1] += 2
    return grid

def turnOff(grid, corner1, corner2):
    grid[corner1[1]:corner2[1]+1, corner1[0]:corner2[0]+1] = np.maximum(grid[corner1[1]:corner2[1]+1, corner1[0]:corner2[0]+1] - 1, 0)
    return grid

def doCommand(grid, command, coord1, coord2):
    if command == "turn on":
        return turnOn(grid, coord1, coord2)
    elif command == "turn off":
        return turnOff(grid, coord1, coord2)
    elif command == "toggle":
        return toggle(grid, coord1, coord2)
    else:
        return grid

grid = np.zeros([9, 9], np.dtype(np.int16))
print(grid)

grid = turnOn(grid, (0, 0), (3, 2))
print(grid)

grid = toggle(grid, (0, 0), (9, 3))
print(grid)

grid = doCommand(grid, "turn on", (0, 0), (9, 8))
print("grid")
print(grid)

grid = doCommand(grid, "toggle", (0, 0), (2, 5))
print("grid")
print(grid)

f = open("input.txt", 'r')

grid = np.zeros([1000, 1000], np.dtype(np.int16))

for line in f:
    commands = re.findall(r'turn on|turn off|toggle', line)
    command = commands[0]
    numbers = re.findall(r'\d+', line)
    #print(numbers)
    x1 = int(numbers[0])
    y1 = int(numbers[1])
    x2 = int(numbers[2])
    y2 = int(numbers[3])
    coord1 = (x1, y1)
    coord2 = (x2, y2)
    grid = doCommand(grid, command, coord1, coord2)


print(grid.sum())


