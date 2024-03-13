def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if sentence == None:
        first = None
        return (length, First)
    else:
        return (length, first)
