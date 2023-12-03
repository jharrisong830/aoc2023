import re

TEXT_TO_NUM = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
DIGITS_PATTERN = r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|[0-9]))"


def sumOfCodesWithText(data: [str]) -> int:
    ans = 0
    for string in data:
        m = re.findall(DIGITS_PATTERN, string)
        dig1, dig2 = m[0], m[-1]
        
        if len(dig1) != 1:
            dig1 = TEXT_TO_NUM[dig1]
        if len(dig2) != 1:
            dig2 = TEXT_TO_NUM[dig2]

        num = dig1 + dig2
        ans += int(num)
    return ans

    


if __name__ == "__main__":
    data = []
    with open("input1.txt", "r") as f:
        for line in f:
            data.append(line)

    ans = sumOfCodesWithText(data)
    print(f"Part 2 answer: {ans}")
    