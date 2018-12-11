import inputreader
import numpy


def distance(a, b):
    #return sum(numpy.abs(b - a))
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_line(line):
    vals = line.split(', ')
    return numpy.array([int(v) for v in vals])


def make_grid(capitals, eval_strat):
    def calc_bounds(capitals):
        vals = numpy.array([c[1] for c in capitals]).transpose()
        bounds = [max(v) - min(v) for v in vals]
        offset = [min(v) for v in vals]
        return offset, bounds

    offset, bounds = calc_bounds(capitals)
    # Adjust the capital coordinates to account for offset
    capitals = [(c[0], c[1] - offset) for c in capitals]
    counts = {c[0]:0 for c in capitals}
    counts['#'] = 0
    edges = set()
    #grid = numpy.full(bounds, -1)

    for x in range(bounds[0]):
        x_edge = (x == 0 or x == bounds[0]-1)
        for y in range(bounds[1]):
            y_edge = (y == 0 or y == bounds[1]-1)
            id = eval_strat(capitals, x, y, counts)
            if id != -1:
                #grid[x, y] = distances[0][0]
                if x_edge or y_edge:
                    edges.add(id)

    return counts, edges


def strategy_a(capitals, x, y, counts):
    distances = [(cap[0], distance([x, y], cap[1])) for cap in capitals]
    s = sorted(distances, key=lambda x: x[1])
    if s[0][1] != s[1][1]:
        counts[s[0][0]] += 1
        return s[0][0]
    else:
        return -1


def strategy_b(capitals, x, y, counts):
    distances = sum([distance([x, y], cap[1]) for cap in capitals])
    if distances < 10000:
        counts['#'] += 1
        return '#'
    return -1


def solve(input, strategy):
    capitals = [(id, parse_line(line)) for (id, line) in enumerate(input.splitlines())]
    counts, edges = make_grid(capitals, strategy)
    valid_states = {c:counts[c] for c in counts if c not in edges}
    biggest = max(valid_states, key=lambda x: valid_states[x])
    return valid_states[biggest]


def part1(input):
    return solve(input, strategy_a)


def part2(input):
    return solve(input, strategy_b)


if __name__ == "__main__":
    input = inputreader.read2018('day6.txt')
    # import timeit
    # def profile():
    #     print(part1(input))
    # print(timeit.timeit(profile, number=1))
    print(part1(input))
    print(part2(input))