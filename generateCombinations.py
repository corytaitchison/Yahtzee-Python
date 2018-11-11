file = open("combinations.txt", "w")
cases = []
k = 6
for a in range(k):
    for b in range(k):
        for c in range(k):
            for d in range(k):
                for e in range(k):
                    for f in range(k):
                        if (a+b+c+d+e+f) == 5:
                            cases.append("0" + str(a)+str(b)+str(c)+str(d)+str(e)+str(f))

output = ", ".join(cases)
file.write(output)
