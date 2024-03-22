from itertools import combinations

ADJ = [          (0, -1),
       (-1, 0),           (1, 0),
                 (0, 1)          ]


def scanRows(galaxies: list[str]) -> list[int]:
    emptyRows = []
    for i in range(len(galaxies)):
        if galaxies[i].find("#") == -1:
            emptyRows.append(i)
    return emptyRows


def scanCols(galaxies: list[str]) -> list[int]:
    emptyCols = []
    strLen = len(galaxies[0])
    broke = False
    for i in range(strLen):
        broke = False
        for j in range(len(galaxies)):
            if galaxies[j][i] == "#":
                broke = True
                break
        if broke:
            continue
        else:
            emptyCols.append(i)
    return emptyCols


def insertEmptySpace(emptyRows: list[int], emptyCols: list[int], galaxies: list[str]) -> list[str]:
    for i in sorted(emptyRows, reverse=True):
        for _ in range(9):
            galaxies.insert(i, "."*len(galaxies[i]))
    for i in sorted(emptyCols, reverse=True):
        for j in range(len(galaxies)):
            galaxies[j] = galaxies[j][:i+1] + "."*9 + galaxies[j][i+1:]
    return galaxies


def getGalaxyCoords(galaxies: list[str]) -> list[tuple[int, int]]:
    coords = []
    for y in range(len(galaxies)):
        for x in range(len(galaxies[y])):
            if galaxies[y][x] == "#": 
                coords.append((x, y))
    return coords


def getGalaxyCoordCombos(coords: list[tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    return list(combinations(coords, 2))


def getAdj(pos: tuple[int, int], goal: tuple[int, int], verticalLen: int, horizontalLen: int) -> list[tuple[int, int]]:
    return list(filter(lambda p: (0 <= p[0] < horizontalLen) and (0 <= p[1] < verticalLen) and (abs(goal[0] - pos[0]) >= abs(goal[0] - p[0])) and (abs(goal[1] - pos[1]) >= abs(goal[1] - p[1])), [(pos[0] + dx, pos[1] + dy) for (dx, dy) in ADJ]))


def bfs(start: tuple[int, int], dst: tuple[int, int], verticalLen: int, horizontalLen: int, emptyRows: list[int], emptyCols: list[int]) -> int:
    if start[0] == dst[0]: return abs(dst[1] - start[1])
    elif start[1] == dst[1]: return abs(dst[0] - start[0])
    previous = {start: None}
    visited = [start]
    queue = [start]
    count = 0
    while len(queue) != 0:
        curr = queue.pop(0)
        if curr == dst or curr[0] == dst[0] or curr[1] == dst[1]:
            count = abs(dst[1] - curr[1]) if curr[0] == dst[0] else abs(dst[0] - curr[0]) if curr[1] == dst[1] else 0
            while previous[curr] != None:
                curr = previous[curr]
                count += 1
            return count
        adjacent = getAdj(curr, dst, verticalLen, horizontalLen)
        for n in adjacent:
            if n not in visited:
                visited.append(n)
                queue.append(n)
                previous[n] = curr
    return -1

        




if __name__ == "__main__":
    inputData = []
    with open("./sample.txt", "r") as f:
        inputData = f.read().splitlines()

    eR = scanRows(inputData)
    eC = scanCols(inputData)
    newGrid = insertEmptySpace(eR, eC, inputData)

    for row in inputData:
        print(row)

    allPairs = getGalaxyCoordCombos(getGalaxyCoords(inputData))
    part1Ans = 0
    for (src, dst) in allPairs:
        part1Ans += (x := bfs(src, dst, len(inputData), len(inputData[0]), eR, eC))
        print(f"between {(src, dst)} is {x} steps")

    print(f"Part 1 answer: {part1Ans}")
