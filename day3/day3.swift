import Foundation


func getInputFromFile(path: String) -> [[Character]] {
    let fm = FileManager.default
    if let fData = fm.contents(atPath: path) {
        guard let fullString = String(data: fData, encoding: .utf8) else {
            return []
        }
        return fullString.split(separator: "\n").map { Array(String($0)) }
    }
    return []
}

func getPartNumbers(matrix: inout [[Character]]) -> [Int] {
    var partNums: [Int] = []
    for x in 0..<matrix.count {
        while let y = matrix[x].firstIndex(where: { ($0 != ".") && !$0.isLetter && !$0.isNumber }) {
            matrix[x][y] = "."
            var toCheck = [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1),           (0, 1),
                           (1, -1),  (1, 0),  (1, 1)]
            toCheck.removeAll(where: { coord in 
                (x + coord.0 > matrix.count) || (y + coord.1 > matrix[x].count) || (x + coord.0 < 0) || (y + coord.1 < 0)
            })
            for coord in toCheck {
                if matrix[x + coord.0][y + coord.1].isNumber {
                    var startInd = y + coord.1
                    var endInd = y + coord.1

                    while startInd > 0 && matrix[x + coord.0][startInd-1].isNumber {
                        startInd -= 1
                    }
                    while endInd < matrix[x].count-1 && matrix[x + coord.0][endInd+1].isNumber {
                        endInd += 1
                    }
                    partNums.append(Int(String(matrix[x + coord.0][startInd...endInd]))!)
                    for i in startInd...endInd {
                        matrix[x + coord.0][i] = "."
                    }
                }
            }
        }
    }
    return partNums
}


func getGearRatios(matrix: inout [[Character]]) -> [Int] {
    var ratios: [Int] = []
    var currNums: [Int] = []
    for x in 0..<matrix.count {
        while let y = matrix[x].firstIndex(where: { $0 == "*" }) {
            matrix[x][y] = "."
            var toCheck = [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1),           (0, 1),
                           (1, -1),  (1, 0),  (1, 1)]
            toCheck.removeAll(where: { coord in 
                (x + coord.0 > matrix.count) || (y + coord.1 > matrix[x].count) || (x + coord.0 < 0) || (y + coord.1 < 0)
            })
            currNums = []
            for coord in toCheck {
                if matrix[x + coord.0][y + coord.1].isNumber {
                    if currNums.count == 2 {
                        currNums = []
                        break
                    }
                    var startInd = y + coord.1
                    var endInd = y + coord.1

                    while startInd > 0 && matrix[x + coord.0][startInd-1].isNumber {
                        startInd -= 1
                    }
                    while endInd < matrix[x].count-1 && matrix[x + coord.0][endInd+1].isNumber {
                        endInd += 1
                    }
                    currNums.append(Int(String(matrix[x + coord.0][startInd...endInd]))!)
                    for i in startInd...endInd {
                        matrix[x + coord.0][i] = "."
                    }
                }
            }
            if currNums.count == 2 {
                ratios.append(currNums[0] * currNums[1])
            }
        }
    }
    return ratios
}

func main() {
    var inputData = getInputFromFile(path: "./input.txt")
    let part1Ans = getPartNumbers(matrix: &inputData).reduce(0, { $0 + $1 })
    print("Part 1 answer: \(part1Ans)")

    inputData = getInputFromFile(path: "./input.txt")
    let part2Ans = getGearRatios(matrix: &inputData).reduce(0, { $0 + $1 })
    print("Part 2 answer: \(part2Ans)")
}

main()
