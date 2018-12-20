import collections
import inputreader
import re
import numpy
import plotly


#position=< 21459,  32026> velocity=<-2, -3>

class Point():
    def __init__(self):
        self.pos = None
        self.vel = None


LINE_REGEX = re.compile(r'position=<(.*)> velocity=<(.*)>')
def parse_line(text):
    def read_vals(str):
        return numpy.array([int(s.strip()) for s in str.split(',')])

    line = LINE_REGEX.match(text)
    #parsed = collections.namedtuple('Line', 'pos vel')
    parsed = Point()
    parsed.pos = read_vals(line.group(1))
    parsed.vel = read_vals(line.group(2))
    return parsed


def moved(points, t=1):
    for i in range(len(points)):
        points[i].pos += points[i].vel * t


def move(points, t=1):
    for p in points:
        p.pos += p.vel * t
    return points


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
    best = bounding_area(points)
    graph = None
    step = 1
    start = 10000
    end = 11000
    moved(points, t=start)
    for t in range(start, end, step):
        points = move(points, t=step)
        size = bounding_area(points)
        #print(t, size)
        if size <= best:
            best = size
            best_t = t
            graph = points.copy()
        if size > best:
            break
    graph = move(graph, t=-1)
    return graph, best_t+step


if __name__ == "__main__":
    input = inputreader.read2018('day10.txt')
    img, best = part1(input)
    print(best)
    draw(img)
    #print(part2(input))