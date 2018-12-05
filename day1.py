import inputreader

def solve(input):
    return sum([int(n) for n in input.splitlines()])


if __name__ == "__main__":
    input = inputreader.read2018('day1.txt')
    print(solve(input))