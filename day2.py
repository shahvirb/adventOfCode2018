import inputreader

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


if __name__ == "__main__":
    input = inputreader.read2018('day2.txt')
    print(part1(input))