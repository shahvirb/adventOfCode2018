import inputreader
import collections
import re

LINE_REGEX = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.')

def parse_line(input):
    result = LINE_REGEX.match(input)
    # Step <step1> must be finished before step <step2> can begin
    line = collections.namedtuple('Line', 'step1 step2')
    line.step1 = result.group(1)
    line.step2 = result.group(2)
    return line


class Step:
    def __init__(self, id):
        self.id = id
        self.pre = set() # Steps which should be executed before self
        self.post = set() # Steps which should be executed after self

    def __repr__(self):
        return self.id

    def __lt__(self, other):
        return self.id < other.id

    def _add_step(self, target_set, s): #this should be class static
        if s in target_set:
            raise Exception('Step with s {} already exists as a pre/post step'.format(s.id))
        else:
            target_set.add(s)

    def add_pre_step(self, s):
        self._add_step(self.pre, s)

    def add_post_step(self, s):
        self._add_step(self.post, s)


class StepsGraph:
    def __init__(self, requirements=None):
        #self.steps = {letter:Step(letter) for letter in map(chr, range(ord('A'), ord('Z')+1))}
        self.steps = {}
        if requirements:
            self.add_requirements(requirements)

    def _add_step(self, id):
        # Should be safe to call if step already exists
        if id not in self.steps:
            self.steps[id] = Step(id)

    def add_requirement(self, requirement):
        self._add_step(requirement.step1)
        self._add_step(requirement.step2)
        self.steps[requirement.step2].add_pre_step(self.steps[requirement.step1])
        self.steps[requirement.step1].add_post_step(self.steps[requirement.step2])

    def add_requirements(self, requirements):
        for r in requirements:
            self.add_requirement(r)

    def walk(self):
        available = set([self.steps[s] for s in self.steps if len(self.steps[s].pre) == 0])
        seen = set()

        def step_ready(step, seen):
            for s in step.pre:
                if s not in seen:
                    return False
            return True

        while available:
            step = min(available)
            yield step.id
            seen.add(step)
            new = set([s for s in step.post if step_ready(s, seen)])
            available = (available | new) - seen


def part1(input):
    lines = [parse_line(line) for line in input.splitlines()]
    graph = StepsGraph(lines)
    result = ''.join([step for step in graph.walk()])
    print(len(graph.steps), len(result))
    return result


if __name__ == "__main__":
    input = inputreader.read2018('day7.txt')
    print(part1(input))
    #print(part2(input))