input_data = raw_input('Enter the number sequence: ')

def pairs(data):
    length = len(data)
    for i in range(length):
        yield(data[i], data[(i + length / 2) % length])

total = sum(int(a) for a, b in pairs(input_data) if a == b)

print 'total =', total
