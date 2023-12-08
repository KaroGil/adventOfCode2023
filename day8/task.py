def checkEndPoint(choosen, end):
    if choosen == end:
        return True
    else:
        return False
    
def checkDirection(way):
    if way == "L":
        return 0
    elif way == "R":
        return 1
    
step_count = 0

with open("input.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]
            
    direction = data[0]
    mappings = data[2:]

    _, end = mappings[-1].split(" = ")[1].split(" ")
    end = end.strip("()")
    end = "ZZZ"
    print("end", end)

    print(mappings) 

    first = mappings[0].split(" = ")[0]

    mapped = {}

    for i in range(len(mappings)):
        elem = mappings[i]
        fromElem, toElem = elem.split(" = ")
        print(fromElem, toElem)
        (a,b) = toElem.split(" ")
        toElem = (a.strip("()"),b.strip("()"))

        mapped[fromElem] = toElem

    print(mapped)

    start = "AAA"
    i = 0
    while True:
        way = direction[i%len(direction)]
        toElem = mapped[start]
        choosen = toElem[checkDirection(way)]
        step_count+=1
        i+=1
        choosen = choosen.strip(",")
        start = choosen
        print(step_count)
        if(checkEndPoint(choosen, end)):
            break

print(step_count)