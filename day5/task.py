#check if seed is in range
def checkRange(seed, range):
    if seed >= range[0] and seed <= range[1]:
        return True
    else:
        return False
    

track = 0
locations = []

with open("adventOfCode2023/day5/input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip() != ""]
    seeds, lines = lines[0], lines[1:]
    title, seedNr = seeds.split(": ")
    seedNr = [int(seedNr) for seedNr in seedNr.split(" ")]

    extended_list = [num for start, end in zip(seedNr[::2], seedNr[1::2]) for num in range(start, start + end)]
    print(extended_list)

#     for i in range(len(seedNr)):
#         track = seedNr[i]
#         found = False
#         # print("SEED: ", track)
#         for line in lines:
#             if line[0].isnumeric():
#                 num = [int(x) for x in line.split(" ") if x.isnumeric()]
#                 # print("Check range: " + str(num[0]) + " " + str(num[1]) + " " + str(num[2]) + "")
#                 if checkRange(track, [num[1], num[1]+num[2]]) and not found:
#                     # print("In range")
#                     diff = track - num[1]
#                     track = num[0] + diff
#                     # print(track)
#                     found = True
#             else: 
#                 # print(line if "location" in line else "")
#                 found = False
#         locations.append(track)


# print(min(locations))