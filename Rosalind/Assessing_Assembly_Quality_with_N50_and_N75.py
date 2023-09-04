import math
def read(file_name):
    file = open(file_name, 'r')
    lines = list()
    # read all lines
    for line in file:
        lines.append(line.strip())

    return lines
def NStatistic(strings,x):
    lengths=[len(i) for i in strings]
    total=0
    for length in reversed(sorted(lengths)):
        total+=length
        if total>x*sum(lengths)/100:
            return length


if __name__ == "__main__":
    data = read("22_input.txt")
    # Print output
    with open('22_output.txt', 'w') as outFile:

        print(f"{NStatistic(data,50)} {NStatistic(data,75)}")