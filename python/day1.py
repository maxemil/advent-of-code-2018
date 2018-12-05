def puzzle1():
    state = 0
    changes = [int(c.strip()) for c in open("data/day1.dat")]
    return state + sum(changes)


def puzzle2():
    changes = [int(c.strip()) for c in open("data/day1.dat")]
    state_hist = dict()
    state = 0
    while True:
        for c in changes:
            state += c
            try:
                state_hist[state]
                return state
            except:
                state_hist[state] = True


if __name__ == '__main__':
    answer1 = puzzle1()
    print answer1
    print puzzle2()
