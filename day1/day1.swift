import Foundation

func getInputFromFile(path: String) -> [String] {
    let fm = FileManager.default
    if let fData = fm.contents(atPath: path) {
        guard let fullString = String(data: fData, encoding: .utf8) else {
            return []
        }
        return fullString.split(separator: "\n").map { String($0) }
    }
    return []
}

let sampleData = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

func sumOfCodes(data: [String]) -> Int {
    let digitPairs: [String] = data.map { str in
        let firstVal = str.first(where: {$0.isNumber} )!
        let secondVal = str.last(where: {$0.isNumber} )!
        return String(firstVal) + String(secondVal)
    }
    let digits: [Int] = digitPairs.map { Int($0)! }
    return digits.reduce(0, { $0 + $1 })
}


let textToNum = ["zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"]
let digitsRegex = try NSRegularExpression(pattern: "(?=(" + textToNum.keys.joined(separator: "|") + "|[0-9]))")

func sumOfCodesWithText(data: [String]) -> Int {
    let digitPairs: [String] = data.map { str in
        var regexResult = digitsRegex.matches(in: str, range: NSMakeRange(0, str.count))
        regexResult.sort(by: {$0.range.location < $1.range.location})

        let firstRange = Range(regexResult[0].range, in: str)!
        let secondRange = Range(regexResult[regexResult.count-1].range, in: str)!

        let firstDig = (regexResult[0].range.length != 1 ? textToNum[String(str[firstRange])] : String(str[firstRange]))!
        let secondDig = (regexResult[regexResult.count-1].range.length != 1 ? textToNum[String(str[secondRange])] : String(str[secondRange]))!
        return firstDig + secondDig
    }

    let digits: [Int] = digitPairs.map { Int($0)! }
    return digits.reduce(0, { $0 + $1 })
}






func main() {
    let inputData = getInputFromFile(path: "./input1.txt")
    let part1Ans = sumOfCodes(data: inputData)
    print("Part 1 answer: \(part1Ans)")

    // let part2Ans = sumOfCodesWithText(data: inputData)
    // print("Part 2 answer: \(part2Ans)")
}

main()
