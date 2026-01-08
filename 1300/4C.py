import sys

n = int(sys.stdin.readline())
db = {}
i = 1
for _ in range(n):
    name = sys.stdin.readline().strip()
    if not db.get(name):
        db[name] = 1
        print("OK")
    else:
        new_name = name + str(db.get(name))
        db[new_name] = 1
        db[name] += 1
        print(new_name)

