def concatenateSequence(*args,seperator):
    string = seperator.join(args)
    return string

def concatenateMapping(**kwargs,seperator):
    

print(concatenateSequence(*'일월화수목금토일',seperator=' - '))