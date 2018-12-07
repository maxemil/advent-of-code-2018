def find_reactions(polymer):
    for i in range(0, len(polymer)-1):
        c = polymer[i]
        if c.isupper():
            if polymer[i+1] == c.lower():
                return polymer[0:i]+polymer[i+2:]
        elif c.islower():
            if polymer[i+1] == c.upper():
                return polymer[0:i]+polymer[i+2:]
    return None


def fully_react(polymer):
    while True:
        reacted_polymer = find_reactions(polymer)
        if not reacted_polymer:
            break
        else:
            polymer = reacted_polymer
    return polymer


def puzzle1():
    polymer = open('data/day5.dat').readlines()[0].strip()
    polymer = fully_react(polymer)
    return len(polymer)


def puzzle2():
    polymer = open('data/day5.dat').readlines()[0].strip()
    best_c = ''
    best_length = len(polymer)
    for c in set(polymer.upper()):
        opt_polymer = polymer.replace(c, '')
        opt_polymer = opt_polymer.replace(c.lower(), '')
        opt_polymer = fully_react(opt_polymer)
        if len(opt_polymer) < best_length:
            best_length = len(opt_polymer)
            best_c = c
    return best_c, best_length


if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
