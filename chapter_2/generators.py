def mygenerator(n):
    while n:
        n -= 1
        yield n

if __name__ == '__main__':
    for i in mygenerator(3):
        print(i)

    # calling the generator function does not generate the sequence,
    # but rather creates a generator object
    print(mygenerator(3))

    # to acrivate the generator object, you call next() on it
    gen = mygenerator(3)
    print(next(gen))
    print(next(gen))
    print(next(gen))

