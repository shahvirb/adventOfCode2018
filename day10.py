#import collections
import inputreader
import re
import numpy
import plotly


#position=< 21459,  32026> velocity=<-2, -3>
class Point():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def __repr__(self):
        return '{}, {}'.format(self.pos, self.vel)


LINE_REGEX = re.compile(r'position=<(.*)> velocity=<(.*)>')
def parse_line(text):
    def read_vals(str):
        return numpy.array([int(s.strip()) for s in str.split(',')])

    line = LINE_REGEX.match(text)
    #parsed = collections.namedtuple('Line', 'pos vel')
    parsed = Point(read_vals(line.group(1)), read_vals(line.group(2)))
    return parsed


def move(points, t):
    return [Point(p.pos + t * p.vel, p.vel) for p in points]


def draw(points):
    plotly.offline.plot({
        "data": [
            plotly.graph_objs.Scatter(x=[p.pos[0] for p in points], y=[-p.pos[1] for p in points], mode='markers')
        ],
        "layout": {
            #"width": 400,
            #"height": 400,
            #"xaxis": {"scaleratio":1},
            "yaxis": {"scaleanchor":"x", "scaleratio":1},
        }
    })


def bounding_area(points):
    x_max = float(max(points, key=lambda x: x.pos[0]).pos[0] - min(points, key=lambda x: x.pos[0]).pos[0])
    y_max = float(max(points, key=lambda x: x.pos[1]).pos[1] - min(points, key=lambda x: x.pos[1]).pos[1])
    #print(x_max, y_max)
    return x_max*y_max


def part1(input):
    points = [parse_line(line) for line in input.splitlines()]
    step = 1
    start = 10000
    end = 11000
    best = bounding_area(move(points, start))
    for t in range(start, end, step):
        moved = move(points, t)
        size = bounding_area(moved)
        #print(t, size)
        if size <= best:
            best = size
            best_t = t
            graph = [p for p in moved]
        if size > best:
            break
    #graph = move(graph, t=-1)
    return graph, best_t

NUM_DIVI = 4
def fast_part1(input):
    points = [parse_line(line) for line in input.splitlines()]
    start = 0
    points = move(points, start)
    end = 15000

    def calc_step(start, end):
        return int((end - start) / (NUM_DIVI - 1))

    step = calc_step(start, end)
    while step != 1:
        search = [(t, bounding_area(move(points, t))) for t in [start+a*step for a in range(0, NUM_DIVI)]]
        min_ind = search.index(min(search, key=lambda x: x[1]))
        assert min_ind != 0
        assert min_ind != len(search) - 1
        if step <= 1:
            t = search[min_ind][0]+step
            graph = move(points, t-step)
            return graph, t
        start = search[min_ind-1][0]
        end = search[min_ind+1][0]
        step = calc_step(start, end)
    return None


if __name__ == "__main__":
    input = inputreader.read2018('day10.txt')
    img, best = part1(input)
    draw(img)
    img, best = fast_part1(input)
    print(best)
    #draw(img)
    #print(part2(input))