import Foundation


func getInputFromFile(path: String) -> [[Int]] {
    let fm = FileManager.default
    if let fData = fm.contents(atPath: path) {
        guard let fullString = String(data: fData, encoding: .utf8) else {
            return []
        }
        let lines =  fullString.split(separator: "\n").map { String($0) }
        return lines.map { $0.split(separator: " ").map { Int($0)! } }
    }
    return []
}


func getHistoryPyramid(row: [Int]) -> [[Int]] {
    var allRows: [[Int]] = []
    allRows.append(row)
    while !allRows.last!.allSatisfy( { $0 == 0 }) { // repeat until a row is all 0
        // print(allRows.last!)
        var newRow: [Int] = []
        for i in 0..<allRows.last!.count-1 {
            newRow.append(allRows.last![i+1] - allRows.last![i]) // new row is the difference of the adj. vals in the above row
        }
        allRows.append(newRow)
    }
    return allRows
}


func predictNextVal(row: [Int]) -> Int {
    var allRows = getHistoryPyramid(row: row)

    allRows[allRows.count-1].append(0) // add a trailing 0 to the row of all 0s
    for i in (0..<allRows.count-1).reversed() { // from bottom row up
        let iCount = allRows[i].count
        let nextCount = allRows[i+1].count
        allRows[i].append(allRows[i+1][nextCount-1] + allRows[i][iCount-1]) // append to each row the current last element, with the previous rows last element (this will be the new last element!)
    }
    return allRows.first!.last! // return the last value of the top array (this is the predicted value)
}


func predictPrevVal(row: [Int]) -> Int {
    var allRows = getHistoryPyramid(row: row)

    allRows[allRows.count-1].insert(0, at: 0) // add a leading 0 to the row of all 0s
    for i in (0..<allRows.count-1).reversed() { // from bottom row up
        allRows[i].insert(allRows[i][0] - allRows[i+1][0], at: 0) // insert to start of each row the current first element, minus the previous rows first element (this will be the new first element!)
    }
    return allRows.first!.first! // return the first value of the top array (this is the predicted value)
}


func main() {
    let inputData = getInputFromFile(path: "./input.txt")
    let part1Ans = inputData.reduce(0, { $0 + predictNextVal(row: $1) })
    print("Part 1 answer: \(part1Ans)")

    let part2Ans = inputData.reduce(0, { $0 + predictPrevVal(row: $1) })
    print("Part 2 answer: \(part2Ans)")
}


main()
