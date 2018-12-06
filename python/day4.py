def puzzle1():
    events = dict()
    for line in open('day4.dat'):
        date = line[line.find('[')+1:line.find(']')]
        event = line[line.find(']')+2:-1]
        events[date] = event
    guards = {}
    for date in sorted(events):
        if '#' in events[date]:
            guard = events[date].split()[1][1:]
            try:
                guards[guard]
            except:
                guards[guard] = []
        else:
            guards[guard].append(int(date.split(':')[1]))
    max_guard = ''
    max_sleep = 0
    for guard, sleep in guards.items():
        sum_sleep = sum([sleep[i+1]-sleep[i] for i in range(0,len(sleep),2)])
        if sum_sleep > max_sleep:
            max_sleep = sum_sleep
            max_guard = guard
    minutes = [0 for i in range(0,59)]
    for i in range(0,len(guards[max_guard]), 2):
        for j in range(guards[max_guard][i], guards[max_guard][i+1]):
            minutes[j] += 1
    min_max = 0
    index_max = -1
    for i in range(0,len(minutes)):
        if minutes[i] > min_max:
            min_max = minutes[i]
            index_max = i
    return int(max_guard) * index_max


def puzzle2():
    events = dict()
    for line in open('day4.dat'):
        date = line[line.find('[')+1:line.find(']')]
        event = line[line.find(']')+2:-1]
        events[date] = event
    guards = {}
    for date in sorted(events):
        if '#' in events[date]:
            guard = events[date].split()[1][1:]
            try:
                guards[guard]
            except:
                guards[guard] = []
        else:
            guards[guard].append(int(date.split(':')[1]))
    guard_minutes = {guard:(-1,0) for guard in guards.keys()}
    for k,v in guards.items():
        minutes = [0 for i in range(0,59)]
        for i in range(0,len(v), 2):
            for j in range(v[i], v[i+1]):
                minutes[j] += 1
        min_max = 0
        index_max = -1
        for i in range(0,len(minutes)):
            if minutes[i] > min_max:
                min_max = minutes[i]
                index_max = i
        guard_minutes[k] = (index_max, min_max)
    global_max_min = -1
    global_max_count = -1
    global_max_guard = ''
    for k,v in guard_minutes.items():
        if v[1] > global_max_count:
            global_max_min = v[0]
            global_max_count = v[1]
            global_max_guard = k
    return int(global_max_guard) * global_max_min

if __name__ == '__main__':
    print(puzzle1())
    print(puzzle2())
