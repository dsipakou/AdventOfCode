line = input()


def find_sum(new_line):
    garbage = False
    level = 0
    output = 0
    index = 0
    while index < len(new_line):
        if new_line[index] == '!':
            index += 2
        elif garbage:
            if new_line[index] == '>':
                index += 1
                garbage = False
            else:
                output += 1
                index += 1

        elif new_line[index] == '{':
            level += 1
            index += 1
        elif new_line[index] == '<':
            garbage = True
            index += 1
        elif new_line[index] == '}':
            level -= 1
            index += 1
        else:
            index += 1

    print(output)


find_sum(line)
