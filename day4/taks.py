suma = 0

with open("adventOfCode2023/day4/input.txt") as f:

    card_pile = {key: 1 for key in range(1, 206)}

    for line in f:
        print(line)
        #setting the variables
        count = 0

        #splitting the line into the card number and the card
        cardNr, card = line.split(": ")

        cardNr = cardNr.strip()
        cardName, cardID = cardNr.split()
        cardID = int(cardID)
        
        #splitting the card into the winning and your card
        winning, your = card.split(" | ")

        #removing the spaces
        winning = winning.strip()
        your = your.strip()

        #splitting the cards into a list of chars
        winning = winning.split(" ")
        your = your.split(" ")

        #cleaning the list from non numeric values
        winning = [int(x) for x in winning if x.isnumeric()]
        your = [int(x) for x in your if x.isnumeric()]

        for i in your:
            if i in winning:
                count += 1

        if count > 0:
            suma += 2**(count-1)
        print("sum", suma)

        for j in range(count):
            card_pile[cardID+j+1] += 1*card_pile[cardID]


print(suma)

total = sum(value for value in card_pile.values())
print("Part 2", total)
