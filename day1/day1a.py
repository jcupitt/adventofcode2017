input_data = raw_input('Enter the number sequence: ')

def pairs(data):
    previous = data[0]
    for x in data[1:]:
        yield(previous, x)
        previous = x
    yield(previous, data[0])

total = sum(int(a) for a, b in pairs(input_data) if a == b)

print 'total =', total
