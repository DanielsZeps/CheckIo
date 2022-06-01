def returnKey(key):
    text = "abcdefghijklmnopqrstuvwxyz0123456789"
    text1 = []
    keys = []
    for x in key:
        try:
            p = keys.index(x)
        except:
            keys.extend(x)
    for x in text:
        try:
            p = keys.index(x)
        except:
            keys.extend(x)
    for x in text.split():
        text1.extend(x)
    return keys

def encode(message, key):
    text1 = []
    text2 = ""
    for x in message.lower():
        y = ord(x)
        z = x if (y < 123 and 96 < y) or (y < 58 and 47 < y) else ""
        if z != "":
            if x == text2:
                text2 += "z" if x == "x" else "x"
                text1.extend([text2])
                text2 = x
            elif len(text2) == 1:
                text1.extend([text2 + x])
                text2 = ""
            else:
                text2 = x
    else:
        if len(text2) == 1:
            text1.extend([text2 + "z"])
    keys = returnKey(key)
    text = ""
    for z in text1:
        x = keys.index(z[0:1])
        y = keys.index(z[1:2])
        if x % 6 == y % 6:
            text += keys[x % 6 + ((x // 6 + 1) % 6) * 6]
            text += keys[y % 6 + ((y // 6 + 1) % 6) * 6]
        elif x // 6 == y // 6:
            text += keys[(x // 6) * 6 + ((x % 6 + 1) % 6)]
            text += keys[(y // 6) * 6 + ((y % 6 + 1) % 6)]
        else:
            text += keys[(x // 6) * 6 + y % 6]
            text += keys[(y // 6) * 6 + x % 6]
    return text


def decode(secret_message, key):
    keys = returnKey(key)
    text = ""
    for d in range(0, round(len(secret_message) / 2)):
        z = secret_message[d*2:d*2+2]
        x = keys.index(z[0:1])
        y = keys.index(z[1:2])
        if x % 6 == y % 6:
            text += keys[x % 6 + ((x // 6 - 1) % 6) * 6]
            text += keys[y % 6 + ((y // 6 - 1) % 6) * 6]
        elif x // 6 == y // 6:
            text += keys[(x // 6) * 6 + ((x % 6 - 1) % 6)]
            text += keys[(y // 6) * 6 + ((y % 6 - 1) % 6)]
        else:
            text += keys[(x // 6) * 6 + y % 6]
            text += keys[(y // 6) * 6 + x % 6]
    return text
