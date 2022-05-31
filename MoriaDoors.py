def find_word(message):
    wordList = {}
    z = 0
    for x in message.split(" "):
        z += 1
        for y in [".", ",", "?", "!"]:
            if y == x[-1::]:
                y = True
                break
        if y == True:
            x = x[0:-1].lower()
        else:
            x = x.lower()
        try:
            wordList[x]["ammount"] += 1
            wordList[x]["order"] = z
        except:
            wordList[x] = {"ammount": 1, "values": [], "order": z}
    z = 0
    average = [-1, None]
    for x in wordList:
        c = 0
        for y in wordList:
            if c < z:
                c += 1
                continue
            if x == y:
                wordList[x]["values"].extend([100] * (wordList[x]["ammount"] - 1))
            else:
                comparison = 0
                comparison += 10 if x[0:1] == y[0:1] else 0
                comparison += 10 if x[-1::] == y[-1::] else 0
                comparison += len(x)/len(y)*30 if len(x) <= len(y) else len(y)/len(x)*30
                letters = []
                unique = []
                for d in x:
                    try:
                        try:
                            p = letters.index(d)
                        except:
                            p = unique.index(d)
                    except:
                        try:
                            p = y.index(d)
                            letters.extend([d])
                            unique.extend([d])
                        except:
                            unique.extend([d])
                for d in y:
                    try:
                        p = unique.index(d)
                    except:
                        unique.extend([d])
                comparison += len(letters) / len(unique) * 50
                wordList[x]["values"].extend([comparison] * (wordList[y]["ammount"]))
                wordList[y]["values"].extend([comparison] * (wordList[x]["ammount"]))
        z += 1
        d = sum(wordList[x]["values"]) / len(wordList[x]["values"])
        if d > average[0]:
            average = [d, x]
        elif d == average[0]:
            if wordList[x]["order"] > wordList[average[1]]["order"]:
                average = [d, x]
    return average[1]
