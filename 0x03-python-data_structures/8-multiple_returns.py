def multiple_returns(sentence):
    if sentence is None:
        first = None
        length = len(sentence)
        newtup = (length, first)
    else:
        first = sentence[0]
        length = len(sentence)
        newtup = (length, first)
    return (newtup)
