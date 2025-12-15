

def square_pool(coordinates, pockets, bounds):
    potted = 0
    looped = 0
    state = 0
    while potted + looped < len(coordinates):
        state += 1
        for n, info in coordinates.items():
            if not info["out"]:
                xi, yi, dx, dy = info["current_state"]
                if (xi, yi, dx, dy) in info["history"]:
                    looped += 1
                    info["out"] = True
                info["history"].append((xi, yi, dx, dy))
                xi += .5 * dx
                yi += .5 * dy
                if (xi, yi) in pockets:
                    potted += 1
                    info["out"] = True
                    continue
                else:
                    if xi in bounds:
                        dy *= -1
                    if yi in bounds:
                        dx *= -1
                info["current_state"] = (xi, yi, dx, dy)
    return potted


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, s = [int(num) for num in input().split()]
        pockets = [(0,0), (0,s), (s,0), (s,s)]
        bounds = [0,s]
        c = {}
        for i in range(n):
            dx, dy, xi, yi = [int(num) for num in input().split()]
            c[i] = {"current_state": (xi, yi, dx,dy)}
            c[i]["history"] = []
            c[i]["out"] = False
        print(square_pool(c, pockets, bounds))