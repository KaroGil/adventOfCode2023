with open("input.txt") as f:
    lines = f.readlines()

count = 0
# TEST_DATA = '''-1 -4 -6 -5 1 14 36 69 115 176 254 351 469 610 776 969 1191 1444 1730 2051 2409'''
# lines = TEST_DATA.splitlines()
lines = [x.strip() for x in lines]

def getDiff(num1, num2):
    return num2-num1

def addNums(num1, diff):
    return num1+diff
def subNums(num1, diff):
    return num1-diff 

def getDiffs(n):
    diffs = n
    while not all(x == 0 for x in diffs):
        diffs = []
        for i in range(len(n)-1):
            diffs.append(getDiff(n[i], n[i+1]))   
        n = diffs
        diffsList.append(diffs)
        
#we have to work thru every line and then store the number in the count variable to get the ans
for line in lines:
    diffsList = []
    print("Start")
    #clean up nums
    nums = line.split(" ")
    nums = [int(x) for x in nums]

    #reverse the list
    nums = nums[::-1]

    diffsList.append(nums)
    #get the differences between each number until we get to 0
    getDiffs(nums)
    print(diffsList)

    #extrapolate
    for i in range(len(diffsList)-3,-1,-1):
        diffsList[i].append(addNums(diffsList[i][-1], diffsList[i+1][-1]))
        print(diffsList[i])
        if diffsList[i][-1] == nums[-1]:
            print("found it")
            print(diffsList[i][-1])
            count += diffsList[i][-1]
            break
    


print(count)
