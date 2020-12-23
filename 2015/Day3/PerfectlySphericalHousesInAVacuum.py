def getNewLocation(location, direction):
    newLocation = location.copy()
    if direction == '>':
        newLocation[0] += 1
    elif direction == '<':
        newLocation[0] -= 1
    elif direction == '^':
        newLocation[1] += 1
    else:
        newLocation[1] -= 1
    return newLocation

currentLocationSanta = [0, 0]
currentLocationRobosanta = [0, 0]

f = open("input.txt", 'r')
directions = f.readline()

visitedLocations = [currentLocationSanta.copy(), currentLocationRobosanta.copy()]

for i in range(0, len(directions), 2):
    currentLocationSanta = getNewLocation(currentLocationSanta, directions[i])
    currentLocationRobosanta = getNewLocation(currentLocationRobosanta, directions[i+1])
    visitedLocations.append(currentLocationSanta.copy())
    visitedLocations.append(currentLocationRobosanta.copy())


visitedLocations = set(tuple(i) for i in visitedLocations)
print(visitedLocations)
print(len(visitedLocations))
