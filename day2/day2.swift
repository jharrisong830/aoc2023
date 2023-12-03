import Foundation

let redLimit = 12
let greenLimit = 13
let blueLimit = 14

struct Round {
    var red: Int = 0
    var green: Int = 0
    var blue: Int = 0

    init(str: Substring) throws {
        let cubes = str.split(separator: ", ")
            let colorMatch = #/([0-9]*) (red|green|blue)/#
            for cube in cubes {
                if let amtColor = try colorMatch.firstMatch(in: cube) {
                    switch amtColor.2 {
                    case "red":
                        self.red += Int(amtColor.1)!
                    case "green":
                        self.green += Int(amtColor.1)!
                    default: // blue
                        self.blue += Int(amtColor.1)!
                    }
                }
            }
    }

    func isPossible() -> Bool {
        return (self.red <= redLimit) && (self.green <= greenLimit) && (self.blue <= blueLimit)
    }
}

struct Game {
    var id: Int = -1
    var rounds: [Round] = []

    init(str: String) throws {
        let strMatch = #/Game ([0-9]*): (.*)/#
        if let match = try strMatch.firstMatch(in: str) {
            self.id = Int(match.1)!
            let rds = match.2.split(separator: "; ")
            self.rounds = try rds.map{ try Round(str: $0) }
        }

    }

    func isValid() -> Bool {
        return self.rounds.map{ $0.isPossible() }.reduce(true, { $0 && $1 })
    }

    func getAllReds() -> [Int] {
        return self.rounds.map{ $0.red }
    }

    func getAllGreens() -> [Int] {
        return self.rounds.map{ $0.green }
    }

    func getAllBlues() -> [Int] {
        return self.rounds.map{ $0.blue }
    }

    func getPower() -> Int {
        return self.getAllReds().max()! * self.getAllGreens().max()! * self.getAllBlues().max()!
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


func sumPossibleGames(data: [String]) -> Int {
    do {
        let games: [Game] = try data.map{ try Game(str: $0) }
        return games.filter{ $0.isValid() }.map{ $0.id }.reduce(0, { $0 + $1 })
    } catch {
        return -1
    }
}

func sumPower(data: [String]) -> Int {
    do {
        let games: [Game] = try data.map{ try Game(str: $0) }
        return games.map{ $0.getPower() }.reduce(0, { $0 + $1 })
    } catch {
        return -1
    }
}


func main() {
    let inputData = getInputFromFile(path: "./input.txt")
    let part1Ans = sumPossibleGames(data: inputData)
    print("Part 1 answer: \(part1Ans)")

    let part2Ans = sumPower(data: inputData)
    print("Part 2 answer: \(part2Ans)")
}

main()
