def multiple_returns(sentence):
    if sentence is None:
        first = None
        length = 0
        newtup = (length, first)
    else:
        first = sentence[0]
        newtup = (len(sentence), first)
    return (newtup)
