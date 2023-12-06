ways = []
with open("adventOfCode2023/day6/input.txt") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    title, times = lines[0].split(": ")
    titleDistance, distances = lines[1].split(": ")

    times = [int(x) for x in times.split(" ") if x != ""]
    distances = [int(x) for x in distances.split(" ") if x != ""]

    for i in range(len(times)):
        time = times[i]
        beaten = []
        for milisecondsHeld in range(time):
            milisecondsLeft = time - milisecondsHeld
            distanceObtained = milisecondsHeld * milisecondsLeft
            if distanceObtained > distances[i]:
                beaten.append(milisecondsHeld)

        ways.append(len(beaten))

print(ways)
product = 1
for i in ways:
    product = product * i

print(product)