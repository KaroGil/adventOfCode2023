sum = 0

digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("adventOfCode2023/day1/input.txt") as f:
    for line in f:
        num = []

        for i in digits.keys():
            if i in line:
                line = line.replace(i, i+str(digits[i])+i)
        print(line)
        for c in line:
            if c.isnumeric():
                num.append(c)
        print(num)
        sum += int(num[0] + num[-1])
        
print(sum)
