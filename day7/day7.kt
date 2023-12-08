import java.io.File

enum class Hand {
    HIGH, PAIR, TWOPAIR, THREEOF, FULLHOUSE, FOUROF, FIVEOF
}

enum class Card {
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE
}


fun handBidPair(line: String): Pair<String, Int> {
    val splitStr = line.split(" ")
    return Pair(splitStr.get(0), splitStr.get(1).toInt())
}


fun parseFile(path: String): List<Pair<String, Int>> {
    val fileLines = File(path).readLines()
    return fileLines.map { handBidPair(it) }
}

fun chrToCard(chr: Char): Card {
    return when (chr) {
        '2' -> Card.TWO
        '3' -> Card.THREE
        '4' -> Card.FOUR
        '5' -> Card.FIVE
        '6' -> Card.SIX
        '7' -> Card.SEVEN
        '8' -> Card.EIGHT
        '9' -> Card.NINE
        'T' -> Card.TEN
        'J' -> Card.JACK
        'Q' -> Card.QUEEN
        'K' -> Card.KING
        'A' -> Card.ACE
        else -> throw Exception("Unexpected input")
    }
}

fun determineHand(cards: List<Card>): Hand {
    var cardCounts: MutableMap<Card, Int> = mutableMapOf()
    for (card in cards) {
        if (card !in cardCounts) {
            cardCounts.put(card, 1)
        }
        else {
            cardCounts[card] = cardCounts[card]!! + 1 
        }
    }
    if (cardCounts.size == 5) return Hand.HIGH // no repeated cards of any kind
    else if (cardCounts.size == 4) return Hand.PAIR // only possible to have a pair of alike cards
    else if (cardCounts.size == 3) {
        if (cardCounts.values.toSet() == setOf(1, 2, 2)) return Hand.TWOPAIR
        else return Hand.THREEOF // (1, 1, 3)
    }
    else if (cardCounts.size == 2) { // full house or 4 of a kind
        return when (cardCounts.values.toSet()) {
            setOf(2, 3) -> Hand.FULLHOUSE // 2, 3 implies full house
            else -> Hand.FOUROF // 1, 4 implies four of a kind
        }
    }
    else return Hand.FIVEOF // cardCounts.size == 1, 5 of a kind
}


fun determineHandWithJokers(cards: List<Card>): Hand {
    var cardCounts: MutableMap<Card, Int> = mutableMapOf()
    for (card in cards) {
        if (card !in cardCounts) {
            cardCounts.put(card, 1)
        }
        else {
            cardCounts[card] = cardCounts[card]!! + 1 
        }
    }
    val jokers = cardCounts[Card.JACK] ?: 0
    if (Card.JACK in cardCounts) cardCounts.remove(Card.JACK)

    if (cardCounts.size == 5) return Hand.HIGH // five different cards, no jokers possible
    else if (cardCounts.size == 4) { // four types of cards, 1 joker possible
        if (jokers == 0) return Hand.PAIR // no jokers -> only possible to have a pair with 5 cards
        else return Hand.THREEOF // with a joker, we can turn that into a three pair (best possible)
    }
    else if (cardCounts.size == 3) { // 3 types of cards, two jokers possible, 
        if (cardCounts.values.toSet() == setOf(1, 2, 2)) return Hand.TWOPAIR // (3, 1, 1) + 0J -> three of a kind, next branch, (2, 2, 1) + 0J -> two pair
        else return Hand.THREEOF // always three of a kind with joker (2, 1, 1) + 1J, (1, 1, 1) + 2J -> three of a kind
    }
    else if (cardCounts.size == 2) { // 2 types of cards, 3 jokers possible (2, 3)
        return when (cardCounts.values.toSet()) {
            setOf(2, 3), setOf(2, 2) -> Hand.FULLHOUSE // 0J or 1J can build a full house
            else -> Hand.FOUROF // all other combos are four of a kind (0J, 1J, 2J, 3J)
        }
    }
    else return Hand.FIVEOF // cardCounts.size == 1 or 0, all cards are the same, with some jokers possible (auto five of a kind)
}


fun compareHandsByCards(cards1: List<Card>, cards2: List<Card>): Int {
    for (i in 0..<cards1.size) {
        if (cards1[i].ordinal != cards2[i].ordinal) {
            return cards1[i].ordinal - cards2[i].ordinal
        }
    }
    throw Exception("Can't sort these cards (hopefully should not ever reach this)")
}

fun compareHandsWithJokers(cards1: List<Card>, cards2: List<Card>): Int {
    for (i in 0..<cards1.size) {
        val c1Val = if (cards1[i] == Card.JACK) -1 else cards1[i].ordinal
        val c2Val = if (cards2[i] == Card.JACK) -1 else cards2[i].ordinal
        if (c1Val != c2Val) {
            return c1Val - c2Val
        }
    }
    throw Exception("Can't sort these cards (hopefully should not ever reach this)")
}

fun sortHandsByStrength(hands: List<Triple<List<Card>, Hand, Int>>, comparer: Comparator<Triple<List<Card>, Hand, Int>>): List<Triple<List<Card>, Hand, Int>> {
    return hands.sortedWith(comparer)
}

fun getTotalWinnings(sortedHands: List<Triple<List<Card>, Hand, Int>>): Int {
    for (i in 0..<sortedHands.size) {
        val (cards, hand, bid) = sortedHands[i]
        println((i+1).toString() + ".)\t" + cards.toString() + "  " + hand.toString() + "  " + bid.toString())
    }
    val indexedBids = sortedHands.mapIndexed { index: Int, (_, _, bid): Triple<List<Card>, Hand, Int> -> (index + 1) * bid }
    return indexedBids.reduce { acc, x -> acc + x }
}




fun main() {
    val inputData = parseFile("./input.txt")
    val hands = inputData.map { (cardStr, bid): Pair<String, Int> -> Pair(cardStr.map { chr: Char -> chrToCard(chr) }, bid) }.map { (hand, bid): Pair<List<Card>, Int> -> Triple(hand, determineHand(hand), bid) }

    val handComparer = Comparator { (_, h1, _): Triple<List<Card>, Hand, Int>, (_, h2, _): Triple<List<Card>, Hand, Int> -> h1.ordinal - h2.ordinal }
        .then { (c1, _, _): Triple<List<Card>, Hand, Int>, (c2, _, _): Triple<List<Card>, Hand, Int> -> compareHandsByCards(c1, c2) }

    val part1Ans = getTotalWinnings(sortHandsByStrength(hands, handComparer))
    println("Part 1 answer: " + part1Ans)



    val jokerHands = inputData.map { (cardStr, bid): Pair<String, Int> -> Pair(cardStr.map { chr: Char -> chrToCard(chr) }, bid) }.map { (hand, bid): Pair<List<Card>, Int> -> Triple(hand, determineHandWithJokers(hand), bid) }

    val handComparerJoker = Comparator { (_, h1, _): Triple<List<Card>, Hand, Int>, (_, h2, _): Triple<List<Card>, Hand, Int> -> h1.ordinal - h2.ordinal }
        .then { (c1, _, _): Triple<List<Card>, Hand, Int>, (c2, _, _): Triple<List<Card>, Hand, Int> -> compareHandsWithJokers(c1, c2) }

    val part2Ans = getTotalWinnings(sortHandsByStrength(jokerHands, handComparerJoker))
    println("Part 2 answer: " + part2Ans)
}
