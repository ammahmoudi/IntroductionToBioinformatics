
def read(file_name):
    file = open(file_name, 'r')
    lines = list()
    # read all lines
    for line in file:
        lines.append(line.strip())
    return lines[0], lines[1].split(' ')


def last_to_first_mapper(last_column, first_column, location):
    char = last_column[location]
    indices = [i for i, x in enumerate(last_column) if x == char]
    index = indices.index(location)
    indices = [i for i, x in enumerate(first_column) if x == char]
    return indices[index]


def BWMATCHING(FirstColumn, LastColumn, Pattern):
    top = 0
    bottom = len(LastColumn)-1
    while top <= bottom:

        if len(Pattern) > 0:
            # last leetter in the pattern
            symbol = Pattern[-1]
            # remove the last letter from pattern
            Pattern = Pattern[:-1]
            # if positions from top to bottom in LastColumn contain an occurrence of symbol
            if symbol in LastColumn[top:bottom+1]:
                topIndex = LastColumn[top:bottom+1].index(symbol)+top
                tmp_list = LastColumn[top:bottom+1]
                bottomIndex = len(tmp_list) - \
                    tmp_list[::-1].index(symbol) - 1+top
                top = last_to_first_mapper(LastColumn, FirstColumn, topIndex)
                bottom = last_to_first_mapper(
                    LastColumn, FirstColumn, bottomIndex)
            else:
                return 0
        else:
            return bottom-top+1


def BWMATCHING_helper(text, patterns):
    first_column = list(text)
    first_column.sort()
    last_column = list(text)
    result = []
    for pattern in patterns:
        result.append(BWMATCHING(first_column, last_column, pattern))
    return result


if __name__ == "__main__":
    text, patterns = read("24_input.txt")
    result = BWMATCHING_helper(text, patterns)
for i in result:
    print(i, end=" ")
