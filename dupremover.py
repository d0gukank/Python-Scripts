a = list()
with open('d.txt') as f:
        lines = [line.rstrip() for line in f]
        a.append(lines)

#print lines
lines = list(dict.fromkeys(lines))
for l in lines:
        print l
