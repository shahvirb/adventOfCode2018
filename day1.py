import inputreader

def part1(input):
    return sum([int(n) for n in input.splitlines()])


def part2(input):
    sum = 0
    freqs = set([sum])
    vals = [int(l) for l in input.splitlines()]
    while True: #TODO not very safe if frequency doesn't repeat
        for n in vals:
            sum += n
            if sum in freqs:
                return sum
            else:
                freqs.add(sum)
    return None


if __name__ == "__main__":
    input = inputreader.read2018('day1.txt')
    print(part1(input))
    print(part2(input))