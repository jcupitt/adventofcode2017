total = 0

with open('input', 'r') as f:
    for line in f:
        numbers = [int(x) for x in line.split()]
        total += (a / b for a in numbers for b in numbers 
                  if a != b and a % b == 0).next()

print 'total =', total
