ADJ = [          (-1, 0),
       (0, -1),           (0, 1),
                 (1, 0)]







def getLoop(start: tuple[int, int], graph: list[str]):
    currNodes = []
    visited = [start]
    x, y = start
    for dx, dy in ADJ:
        match graph[x + dx][y + dy]:
            case "|" if dy == 0: # above or below the start
                currNodes.append((x + dx, y + dy))
            case "-" if dx == 0: # left or right of the start
                currNodes.append((x + dx, y + dy))
            case "L" if (dx, dy) == (0, -1) or (dx, dy) == (1, 0): # below or to the left
                currNodes.append((x + dx, y + dy))
            case "7" if (dx, dy) == (0, 1) or (dx, dy) == (-1, 0): # above or to the right
                currNodes.append((x + dx, y + dy))
            case "J" if (dx, dy) == (0, 1) or (dx, dy) == (1, 0): # below or to the right
                currNodes.append((x + dx, y + dy))
            case "F" if (dx, dy) == (0, -1) or (dx, dy) == (-1, 0): # above or to the left
                currNodes.append((x + dx, y + dy))


    count = 1
    while currNodes != []:
        # print(f"Count: {count}, Current nodes to check: {currNodes}")
        toDelete = []
        for i in range(len(currNodes)):
            x, y = currNodes[i]
            # print(f"({x}, {y}) -> {graph[x][y]}")
            if (x, y) in visited:
                toDelete.append((x, y))
                continue
            if (x, y) == start:
                toDelete.append((x, y))
                continue
            visited.append((x, y))
            match graph[x][y]:
                case "|" if (x + 1, y) not in visited:
                    currNodes[i] = (x + 1, y)
                case "|" if (x - 1, y) not in visited:
                    currNodes[i] = (x - 1, y)
                case "-" if (x, y - 1) not in visited:
                    currNodes[i] = (x, y - 1)
                case "-" if (x, y + 1) not in visited:
                    currNodes[i] = (x, y + 1)
                case "J" if (x - 1, y) not in visited:
                    currNodes[i] = (x - 1, y)
                case "J" if (x, y - 1) not in visited:
                    currNodes[i] = (x, y - 1)
                case "L" if (x - 1, y) not in visited:
                    currNodes[i] = (x - 1, y)
                case "L" if (x, y + 1) not in visited:
                    currNodes[i] = (x, y + 1)
                case "7" if (x, y - 1) not in visited:
                    currNodes[i] = (x, y - 1)
                case "7" if (x + 1, y) not in visited:
                    currNodes[i] = (x + 1, y)
                case "F" if (x + 1, y) not in visited:
                    currNodes[i] = (x + 1, y)
                case "F" if (x, y + 1) not in visited:
                    currNodes[i] = (x, y + 1)
                case "X" | _ : toDelete.append((x, y))
            count += 1
            graph[x] = graph[x][:y] + "X" + graph[x][y+1:]


        for item in toDelete:
            # print(f"removing {item} from {toDelete}")
            currNodes.remove(item)
        

    return count // 2






if __name__ == "__main__":
    inputData = ""
    with open("./input.txt", "r") as f:
        inputData = f.read()

    inputData = inputData.splitlines()
    
    # for row in inputData:
    #     print(row)

    S = (-1, -1)
    for i in range(len(inputData)):
        y = inputData[i].find("S")
        if y != -1:
            S = (i, y)
            break

    part1Ans = getLoop(S, inputData)
    print(f"Part 1 answer: {part1Ans}")


    