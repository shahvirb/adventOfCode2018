import inputreader
import numpy as np


def checksum(code):
    counts_dict = {}
    for c in code:
        if c not in counts_dict:
            counts_dict[c] = 1
        else:
            counts_dict[c] += 1
    return counts_dict


def part1(input):
    twos = 0
    threes = 0
    for line in input.splitlines():
        csum = checksum(line)
        counts = list(csum.values())
        if 2 in counts:
            twos += 1
        if 3 in counts:
            threes += 1
    return twos * threes


def part2(input):
    def check(id1, id2):
        return (id1 == id2).sum() == len(id1) - 1

    chars = [np.array(list(line)) for line in input.splitlines()]
    for line1 in chars:
        for line2 in chars:
            if line1 is not line2 and check(line1, line2):
                common = np.ma.masked_array(line1, (line1 != line2)).compressed()
                return ''.join(common) #line1, line2
    return None


if __name__ == "__main__":
    input = inputreader.read2018('day2.txt')
    print(part1(input))
    print(part2(input))