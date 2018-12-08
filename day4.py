import inputreader
import re
import collections

LINE_REGEX = re.compile(r'\[([\d]*)-([\d]*)-([\d]*) ([\d]*):([\d]*)\] (.*)')
GUARD_REGEX = re.compile(r'Guard #([\d]*)')

def parse_line(line):
    result = LINE_REGEX.match(line)
    parsed = collections.namedtuple('Line', 'year month day hour min text guard')
    parsed.year = result.group(1)
    parsed.month = result.group(2)
    parsed.day = result.group(3)
    parsed.hour = result.group(4)
    parsed.min = result.group(5)
    parsed.text = result.group(6)
    try:
        parsed.guard = GUARD_REGEX.match(parsed.text).group(1)
    except AttributeError:
        parsed.guard = None

    return parsed


class Guard:
    def __init__(self, id):
        self.id = id
        self.mins_asleep = []

    def sleep(self, min):
        self._sleep_start = min

    def wake(self, min):
        self.slept(self._sleep_start, min)
        self._sleep_start = None

    def slept(self, start, stop):
        for i in range(int(start), int(stop)):
            self.mins_asleep.append(i)

    def total_mins_slept(self):
        return len(self.mins_asleep)

    def most_slept_min(self):
        count = collections.Counter(self.mins_asleep)
        return count.most_common(1)[0][0]


def gen_guards(input):
    parsed = [parse_line(line) for line in sorted(input.splitlines())]
    guards = {}
    current_g = None
    for line in parsed:
        if line.guard:
            if current_g:
                guards[current_g.id] = current_g
            current_g = guards.get(line.guard, Guard(line.guard))
        else:
            if 'asleep' in line.text:
                current_g.sleep(line.min)
            else:
                current_g.wake(line.min)
    return guards


def part1(input):
    guards = gen_guards(input)
    # execute strategy 1
    target = sorted(guards.values(), key=lambda x : x.total_mins_slept(), reverse=True)[0] #highest slept is first
    return int(target.id) * target.most_slept_min()


def part2(input):
    guards = gen_guards(input)
    target = sorted(guards.values(), key=lambda x : -99 if not x.mins_asleep else collections.Counter(x.mins_asleep).most_common(1)[0][1], reverse=True)[0] #highest slept is first
    return int(target.id) * collections.Counter(target.mins_asleep).most_common(1)[0][0]


if __name__ == "__main__":
    input = inputreader.read2018('day4.txt')
    print(part1(input))
    print(part2(input))