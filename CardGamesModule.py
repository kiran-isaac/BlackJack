def pickRandomCard(excluded = []):
    import random
    card = ""
    suitList = ["Spades","Clubs","Diamonds","Hearts"]
    cardList = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
    card = str(random.choice(cardList)) + " of " + str(random.choice(suitList))
    while card in excluded:
        card = str(random.choice(cardList)) + " of " + str(random.choice(suitList))
    return card
    

def getCardNo(x):
    output = []
    try:
        x.append("List test")
        x.remove("List test")
        for i in range(len(x)):
            card = str((x[i:i+1]))
            cardVal = card[2:card.find(" ")]
            output.append(cardVal)
    except:
        output = x[:x.find(" ")]
    return output

def pushChoice(message,choices,lowerLimit="",upperLimit="",exceptions=[]):
    while True:
        x = input(message)
        if choices == "integer":
            try:
                x = int(x)
                if upperLimit != "" and lowerLimit != "":
                    if x <= upperLimit and x >= lowerLimit:
                        if not x in exceptions:
                            return x
                        else:
                            print("You cannot choose the number %s " % (str(x)))
                    else:
                        print("Please enter a whole number between",lowerLimit,"and",upperLimit)
            except:
                print("Please enter a number")
        
        elif choices == "float":
            try:
                x = float(x)
                if upperLimit != "" and lowerLimit != "":
                    if x <= upperLimit and x >= lowerLimit:
                        if not x in exceptions:
                            return x
                        else:
                            print("You cannot choose the number %s " % str(x))
                    else:
                        print("Please enter a number between",lowerLimit,"and",upperLimit)
            except:
                print("Please enter a number")

        else:
            if x in choices:
                return x

def suitNameToAsciiChar(y):
    y = y.lower()
    if y == "spades":
        y = "♠"
    elif y == "clubs":
        y = "♣"
    elif y == "diamonds":
        y = "♦"
    else:
        y = "♥"
    return y   

def getCardVals(cards,i):
    x = str(str((cards[i:i+1]))[2:len(cards[i:i+1])-3])
    y = suitNameToAsciiChar(getCardNo(x))
    y = x[x.find("of ")+3:]
    y = suitNameToAsciiChar(y)
    x = getCardNo(x)
    if x != "10":
        x = x[:1]
    else:
        x = x[:2]
    return x,y

def printCardList(cards,gaps = 0,showNos = False,noStart = 0):
    cards = [card.upper() for card in cards]
    z = gaps
    cardCount = noStart
    if showNos:
        print()
    try:
        cards.append(1)
        cards.remove(1)
    except:
        cards = [cards]
    gaps = ""
    for i in range(z):
        gaps = str(gaps) + " "
    for i in range(len(cards)):
        j = i
        if not showNos:
            print(" _____ ",end=gaps)
        else:
            j=j+cardCount
            print(j+1,end="")
            for j in range(6-len(str(i+1))):
                print("_",end="")
            print(" ",end=gaps)
    print()

    ####################################### Line 2

    for i in range(len(cards)):
        x,y = getCardVals(cards,i)
        try:
            x = int(x)
            if x != 10:
                print("|" + str(x) + "    |",end=gaps)
            else:
                print("|" + str(x) + " " + y + " |",end=gaps)
        except:
            if x != "A":
                x = str(x)
                print("|" + str(x) + " ww |",end=gaps)
            else:
                if y == "♠":
                    print("|A .  |",end=gaps)
                elif y == "♣":
                    print("|A _  |",end=gaps)
                elif y == "♦":
                    print("|A ^  |",end=gaps)
                else:
                    print("|A_ _ |",end=gaps)

    ####################################### Line 3

    print()
    for i in range(len(cards)):
        x,y = getCardVals(cards,i)
        try:
            x = int(x)
            if x in [2,3]:
                print("|  %s  |" % y,end=gaps)
            elif x in [4,5,6,7]:
                print("| %s %s |" % (y,y),end=gaps)
            elif x in [8,9,10]:
                print("|%s %s %s|" % (y,y,y),end=gaps)
        except:
            if x != "A":
                x = str(x)
                print("|  () |",end=gaps)
            else:
                if y == "♠":
                    print("| /.\ |",end=gaps)
                elif y == "♣":
                    print("| ( ) |",end=gaps)
                elif y == "♦":
                    print("| / \ |",end=gaps)
                else:
                    print("|( v )|",end=gaps)

    ####################################### Line 4

    print()
    for i in range(len(cards)):
        x,y = getCardVals(cards,i)
        try:
            x = int(x)
            if x in [2,4]:
                print("|     |",end=gaps)
            elif x in [3,5]:
                print("|  %s  |" % y,end=gaps)
            elif x in [6,8]:
                print("| %s %s |" % (y,y),end=gaps)
            else:
                print("|%s %s %s|" % (y,y,y),end=gaps)

        except:
            if x != "A":
                print("|%s/()\|" % y,end=gaps)
            else:
                if y == "♠":
                    print("|(_._)|",end=gaps)
                elif y == "♣":
                    print("|(_'_)|",end=gaps)
                elif y == "♦":
                    print("| \ / |",end=gaps)
                else:
                    print("| \ / |",end=gaps)

    ####################################### Line 5

    print()
    for i in range(len(cards)):
        x,y = getCardVals(cards,i)
        try:
            x = int(x)
            if x in [2,3]:
                print("|  %s  |" % y,end=gaps)
            elif x in [4,5,6,7]:
                print("| %s %s |" % (y,y),end=gaps)
            elif x in [8,9,10]:
                print("|%s %s %s|" % (y,y,y),end=gaps)
        except:
            if x != "A":
                print("|%s || |" % y,end=gaps)
            else:
                if y == "♠":
                    print("|  |  |",end=gaps)
                elif y == "♣":
                    print("|  |  |",end=gaps)
                elif y == "♦":
                    print("|  .  |",end=gaps)
                else:
                    print("|  .  |",end=gaps)

    ####################################### Line 5

    print()
    for i in range(len(cards)):
        x,y = getCardVals(cards,i)
        try:
            x = int(x)
            if x != 10:
                print("|____%s|" % x,end=gaps)
            else:
                print("|___%s|" % x,end=gaps)
        except:
            if x != "A":
                print("|__||%s|" % x,end=gaps)
            else:
                print("|____A|",end=gaps)
    print()

def printCards(cards, perLine = 0, gaps = 0, header = "", showNos=False):
    if type(cards) != list:
        cards = [cards]
    if not perLine:
        perLine = len(cards)
    countProgress = 0
    if header != "":
        totalLength = perLine*7 + (perLine-1)*gaps
        print("".join([" " for i in range((totalLength-len(header))//2)]),end="")
        print(header)
    if not perLine:
        perLine = len(cards)
    while len(cards) > perLine:
        picked = cards[:perLine]
        printCardList(picked,gaps,showNos,countProgress)
        cards = cards[perLine:]
        countProgress += perLine
    printCardList(cards,gaps,showNos,countProgress)