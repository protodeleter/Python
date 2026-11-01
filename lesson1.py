

def exe1(sr: str):
    return sr[::-1]

def exe2(sr: str):

    cc = 0
    ccn = 0
    for c in sr:
        if 'a' <= c <= 'z':
            cc += 1
        elif 'A' <= c <= 'Z':
            cc += 1
        elif '0' <= c <= '9':
            ccn += 1
    print("letters " + str(cc))
    print("numbers " + str(ccn))




def exe3(sr: str, index: int):

    newsr = sr.replace(sr[index], "")
    return newsr

def exe4(sr: str):
    fc = sr[0]
    lc = sr[-1]
    news = sr[:-1]
    news = news[1:]
    news = lc+news+fc
    print(news)


def exe5(sr: str):
    return sr[0::2]

def exe6(tag: str, src: str):
    starting_tag = ["<", tag, ">"]
    ending_tag = ["</", tag, ">"]
    starting_joined = "".join(starting_tag)
    ending_joined = "".join(ending_tag)
    return "".join(starting_joined) + src +"".join(ending_joined)


def exe7(sr: str):
    return sr[len(sr)-2::] * 4

def exe8(sr: str):


    return  sr if len(sr) < 3 else sr[0:3:1]

def exe11(sr: str):
    return "".join(dict.fromkeys(sr))

def exe12(sr: str):
    return "".join(dict.fromkeys(sr))