def requiredPaper(l, w, h):
    m = max(l, w, h)
    return 2 * l * w + 2 * l * h + 2 * w * h + l * w * h / m

print(requiredPaper(2, 3, 4))

def requiredRibbon(l, w, h):
    minPerim = 2 * min(l + w, l + h, w + h)
    return minPerim + l * w * h

print(requiredRibbon(2, 3, 4))

totalRequiredPaper = 0
totalRequiredRibbon = 0

f = open("input.txt", "r")

for line in f:
    line = line.rstrip()
    words = line.split('x')
    [l, w, h] = [int(i) for i in words]
    totalRequiredPaper += requiredPaper(l, w, h)
    totalRequiredRibbon += requiredRibbon(l, w, h)


print(totalRequiredPaper)
print("totalRequiredRibbon = " + str(totalRequiredRibbon))
f.close()