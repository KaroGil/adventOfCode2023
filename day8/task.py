import math

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
    first = mappings[0].split(" = ")[0]

    mapped = {}

    allA = []
    allZ = []

    for i in range(len(mappings)):
        elem = mappings[i]
        fromElem, toElem = elem.split(" = ")
        #print(fromElem, toElem)
        (a,b) = toElem.split(" ")
        toElem = (a.strip("()"),b.strip("()"))

        if "A" in fromElem:
            allA.append(fromElem)
        if "Z" in toElem:
            allZ.append(fromElem)

        mapped[fromElem] = toElem

    #print(mapped)

    #part 1
    # start = "AAA"
    # i = 0
    # while True:
    #     way = direction[i%len(direction)]
    #     toElem = mapped[start]
    #     choosen = toElem[checkDirection(way)]
    #     step_count+=1
    #     i+=1
    #     choosen = choosen.strip(",")
    #     start = choosen
    #     print(step_count)
    #     if(checkEndPoint(choosen, end)):
    #         break

#print(step_count)


#part 2
    def getSteps(startNode):
        count = 0
        while startNode[2] != "Z":
            way = direction[count%len(direction)]
            toElem = mapped[startNode]
            choosen = toElem[checkDirection(way)]
            count+=1
            startNode = choosen.strip(",")
        return count 
        
lengths = [getSteps(x) for x in allA]
print(lengths)

ans = math.lcm(*lengths)
print(ans)