def areYouPlayingBanjo(name):
    n = tuple(name)
    if n[0] == "r" or n[0] == "R":
        return("Rikke plays banjo")
    else:
        return("Martin does not play banjo")
print(areYouPlayingBanjo("h"))
