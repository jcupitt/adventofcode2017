# day3 ... first try, just count outwards

final = int(raw_input('Cell number: '))

# we start at "1", position (0, 0)

#  37 36 35 34 33 32 31
#  38 17 16 15 14 13 30
#  39 18  5  4  3 12 29
#  40 19  6  1  2 11 28
#  41 20  7  8  9 10 27 
#  42 21 22 23 24 25 26
#  43 44 45 46 47 48 49 

# as we spiral outwards, track 
# the current number
# the length of the next side we add 
# the current (x, y) position

current = 1
side = 0
x = 0
y = 0

while True:
    # step out one
    x += 1
    side += 2
    current += 1

    print "{0}: ({1}, {2})".format(current, x, y)

    if current == final:
        break

    # go up to "3"
    current += side - 1
    y += side - 1

    print "{0}: ({1}, {2})".format(current, x, y)

    if current >= final:
        y -= current - final
        break

    # left to "5"
    current += side
    x -= side 

    print "{0}: ({1}, {2})".format(current, x, y)

    if current >= final:
        x += current - final
        break

    # down to "7"
    current += side
    y -= side 

    print "{0}: ({1}, {2})".format(current, x, y)

    if current >= final:
        y += current - final
        break

    # right to "9"
    current += side
    x += side

    print "{0}: ({1}, {2})".format(current, x, y)

    if current >= final:
        x -= current - final
        break

print "{0}: ({1}, {2})".format(final, x, y)

print "steps =", abs(x) + abs(y)
