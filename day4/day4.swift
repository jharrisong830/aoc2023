import Foundation

struct Card {
    var id: Int = 0
    var winning: [Int] = []
    var nums: [Int] = []

    init(str: String) throws {
        let strMatch = #/Card\s+([0-9]*):\s+(.*)/#
        if let match = try strMatch.firstMatch(in: str) {
            self.id = Int(match.1)!
            let allNums = match.2.split(separator: "|")
            self.winning = allNums[0].split(separator: " ").map{ Int($0)! }
            self.nums = allNums[1].split(separator: " ").map{ Int($0)! }
        }
    }

    init(id: Int) {
        self.id = id
    }

    func calculateScore() -> Int {
        let myWinningNumbers = self.nums.filter{ self.winning.contains($0) }
        return myWinningNumbers.count == 0 ? 0 : Int(truncating: NSDecimalNumber(decimal: pow(2, myWinningNumbers.count - 1))) // subtract 1 to start with 2^0 for one element... so on
    }

    func getNumMatches() -> Int {
        return self.nums.filter{ self.winning.contains($0) }.count
    }

}

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


func getNewScore(cards: [Card]) -> Int {
    var winCounts: [Int: Int] = [:]

    func buildDictionary(currCard: Card) -> Int { 
        let count = currCard.getNumMatches()
        guard count > 0 else {
            return 1
        }
        let copyRange = currCard.id+1 ... currCard.id+count
        var acc = 1
        for i in copyRange {
            if let storedVal = winCounts[i] {
                acc += storedVal
            }
            else {
                winCounts[i] = buildDictionary(currCard: cards.first(where: { $0.id == i })!)
                acc += winCounts[i]!
            }
        }
        return acc
    }

    var total = 0
    for i in 1...cards.count {
        if let _ = winCounts[i] {
            continue
        }
        else {
            winCounts[i] = buildDictionary(currCard: cards.first(where: { $0.id == i } )!)
        }
    }

    for card in cards {
        total += winCounts[card.id]!
    }
    return total


    // while !cardQueue.isEmpty {
    //     let currCard = cardQueue.removeFirst()
    //     total += 1
    //     if let count = winCounts[currCard.id] {
    //         if count == 0 {
    //             continue
    //         }
    //         for i in currCard.id+1...currCard.id+count {
    //             cardQueue.append(Card(id: i))
    //         }
    //     }
    //     else {
    //         let count = currCard.getNumMatches()
    //         winCounts[currCard.id] = count
    //         if count == 0 {
    //             continue
    //         }
    //         for i in currCard.id+1...currCard.id+count {
    //             cardQueue.append(Card(id: i))
    //         }
    //     }
    // }
    // return total
}


func main() {
    let inputData = getInputFromFile(path: "./input.txt")
    do {   
        let cards = try inputData.map{ try Card(str: $0) }
        let part1Ans = cards.map{ $0.calculateScore() }.reduce(0, { $0 + $1 })
        print("Part 1 answer: \(part1Ans)")

        let part2Ans = getNewScore(cards: cards)
        print("Part 2 answer: \(part2Ans)")
    } catch {
        print("oopsie!")
    }
}

main()
