def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if sentence == None:
        return (length, None)
    else:
        return (length, first)
