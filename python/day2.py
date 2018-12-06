def puzzle1():
    boxids = [line.strip() for line in open("data/day2.dat")]
    twice = 0
    thrice = 0
    for bid in boxids:
        counts = [bid.count(c) for c in set(bid)]
        if 2 in counts:
            twice += 1
        if 3 in counts:
            thrice +=1
    return twice * thrice

def fuzzy_compare(str1, str2):
    for i in range(0,len(str1),1):
        if str1[0:i-1] == str2[0:i-1] and str1[i:] == str2[i:] and str1[i-1] != str2[i-1]:
            return (True, str1[0:i-1]+str1[i:])
    return (False, '')

def puzzle2():
    boxids = [line.strip() for line in open("data/day2.dat")]
    for bid1 in boxids:
        for bid2 in boxids:
            is_similar, substring = fuzzy_compare(bid1, bid2)
            if is_similar:
                return substring



if __name__ == '__main__':
    print puzzle1()
    print puzzle2()
