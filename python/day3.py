def get_rectangles_fabric():
    rectangles = {}
    for line in open("data/day3.dat"):
        num = line.split('@')[0].strip()[1:]
        offset = [int(x) for x in line.split('@')[1].split(':')[0].split(',')]
        size = [int(x) for x in line.strip().split('@')[1].split(':')[1].split('x')]
        rectangles[num] = offset + size
    xmax = max([x[0]+x[2] for x in rectangles.values()])
    ymax = max([x[1]+x[3] for x in rectangles.values()])
    fabric = [[0] * ymax for i in range(0, xmax)]
    for rect in rectangles.values():
        for x in range(rect[0], rect[0] + rect[2]):
            for y in range(rect[1], rect[1] + rect[3]):
                fabric[x][y] += 1
    return rectangles, fabric


def puzzle1():
    rectangles, fabric = get_rectangles_fabric()
    overlaps = 0
    for x in fabric:
        for y in x:
            if y > 1:
                overlaps += 1
    return overlaps


def puzzle2():
    rectangles, fabric = get_rectangles_fabric()
    for i, rect in rectangles.items():
        overlaps = False
        for x in range(rect[0], rect[0] + rect[2]):
            for y in range(rect[1], rect[1] + rect[3]):
                if fabric[x][y] > 1:
                    overlaps = True
        if not overlaps:
            return i

if __name__ == '__main__':
    print puzzle1()
    print puzzle2()
