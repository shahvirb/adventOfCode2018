import inputreader
import numpy
import re


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
    claims = [Claim(line) for line in input.splitlines()]

    #find the bounding grid size
    #TODO is this necessary?
    width = 0
    height = 0
    for c in claims:
        width = max(width, c.x + c.w)
        height = max(height, c.y + c.h)

    #fill grid
    grid = numpy.zeros([width, height])
    for c in claims:
        grid[c.x:c.x+c.w, c.y:c.y+c.h] += numpy.ones([c.w, c.h])

    #count all the non 0 and non 1 values
    discount = (grid == 0).sum() + (grid == 1).sum()
    result = width * height - discount
    return result


if __name__ == "__main__":
    input = inputreader.read2018('day3.txt')
    print(part1(input))
    #print(part2(input))