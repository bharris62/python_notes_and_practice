def subtractor(a,b):
    ''' I subtract b from a and return result'''
    print("Im a function.  My name is {}".format(subtractor.__name__))
    print("Im about to subtract {} from {}".format(a,b))
    return a - b

if __name__ == '__main__':
    subtractor(3,2)