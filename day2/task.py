red = 12
green = 13
blue = 14

sum = 0

with open('adventOfCode2023/day2/input.txt') as f:
    for line in f:
        l = line.strip()
        game_nr, showed = l.split(": ")

        splits = showed.split(";")

        count = 0
        for split in splits:
            i = split.split(", ")
            a,b,c = 12,13,14
            for j in i:
                if "red" in j:
                    a -= (int(j.split()[0]))
                if "green" in j:
                    b -= (int(j.split()[0]))
                if "blue" in j:
                    c -= (int(j.split()[0]))

            if a < 0 or b < 0 or c < 0:
                count = 1 
        if count == 0:
            sum += int(game_nr.split()[1])   



sum = 0
with open('adventOfCode2023/day2/input.txt') as f:
    for line in f:
        l = line.strip()
        game_nr, showed = l.split(": ")

        splits = showed.split(";")
        max_Red = 0
        max_green = 0
        max_blue = 0

        count = 0
        for split in splits:
            i = split.split(", ")
            a,b,c = 12,13,14
            for j in i:
                if "red" in j and int(j.split()[0]) > max_Red:
                    max_Red = int(j.split()[0])
                if "green" in j and int(j.split()[0]) > max_green:
                    max_green = int(j.split()[0])
                if "blue" in j and int(j.split()[0]) > max_blue:
                    max_blue = (int(j.split()[0]))
        sum+= max_Red*max_green*max_blue
print(sum)