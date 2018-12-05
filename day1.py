import inputreader

def part1(input):
    return sum([int(n) for n in input.splitlines()])


def part2(input):
    sum = 0
    freqs = set([sum])

    while True: #TODO not very safe if frequency doesn't repeat
        for line in input.splitlines():
            sum += int(line)
            if sum in freqs:
                return sum
            else:
                freqs.add(sum)
    return None


if __name__ == "__main__":
    input = inputreader.read2018('day1.txt')
    print(part1(input))
    print(part2(input))