import inputreader

def reacts(a, b):
    return a != b and a.upper() == b.upper()


def react(sequence):
    i = 0
    while i < len(sequence)-1:
        #i = max(0, i)
        curr_char = sequence[i]
        next_char = sequence[i + 1]
        if reacts(curr_char, next_char):
            sequence = sequence[:i] + sequence[i+2:]
            if i != 0: #Don't back-track
                i -= 1
        else:
            i += 1
    return len(sequence) #, ''.join(input)


def part1(input):
    return react(input.strip())


def part2(input):
    input = input.strip()
    units = set([u.upper() for u in input])
    counts = []
    for unit in units:
        sequence = input.replace(unit, '').replace(unit.lower(), '')
        reacted = react(sequence)
        counts.append(reacted)
    return min(counts)


if __name__ == "__main__":
    input = inputreader.read2018('day5.txt')
    print(part1(input))
    print(part2(input))