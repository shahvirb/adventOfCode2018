import inputreader
import numpy
import re

WIDTH = 1000
HEIGHT = 1000

class Claim:
    def __init__(self, descriptor):
        prog = re.compile(r'#([\d]*) @ ([\d]*),([\d]*): ([\d]*)x([\d]*)')
        result = prog.match(descriptor)
        self.id = int(result.group(1))
        self.x = int(result.group(2))
        self.y = int(result.group(3))
        self.w = int(result.group(4))
        self.h = int(result.group(5))


def part1(input):
    def make_grid(claims):
        # find the bounding grid size
        # for c in claims:
        #     width = max(width, c.x + c.w)
        #     height = max(height, c.y + c.h)

        # fill grid
        grid = numpy.zeros([WIDTH, HEIGHT])
        for c in claims:
            grid[c.x:c.x + c.w, c.y:c.y + c.h] += numpy.ones([c.w, c.h])
        return grid

    claims = [Claim(line) for line in input.splitlines()]
    grid = make_grid(claims)

    #count all the non 0 and non 1 values
    discount = (grid == 0).sum() + (grid == 1).sum()
    result = WIDTH * HEIGHT - discount
    return result


def part2(input):
    def make_grid(claims):
        grid = numpy.full((WIDTH, HEIGHT), object)
        grid[...] = [[[] for _ in row] for row in grid]
        for c in claims:
            for i in range(c.x, c.x + c.w):
                for j in range(c.y, c.y + c.h):
                    grid[i, j].append(c.id)
        return grid

    claims = [Claim(line) for line in input.splitlines()]
    grid = make_grid(claims)

    for c in claims:
        overlaps = False
        for i in range(c.x, c.x + c.w):
            for j in range(c.y, c.y + c.h):
                if len(grid[i, j]) != 1:
                    overlaps = True
        if not overlaps:
            return c.id

    return None

if __name__ == "__main__":
    input = inputreader.read2018('day3.txt')
    print(part1(input))
    print(part2(input))