def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if sentence is None:
        first = None
        newtup = (length, first)
        return (newtup)
    else:
        newtup = (length, first)
        return (newtup)
