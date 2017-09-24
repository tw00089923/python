with open("hi.txt","r",encoding="utf-8") as fp:
    raw = fp.readlines()

abs = []

for a in raw:
    abs.append(a.strip().split())
print(abs)


def show():
    i = 0 
    for data in abs:
        print("{:>2}:{:<6}".format(i,data[0]))
        i += 1
show()