def retiring_n(lines):
    lines_treated = []

    for line in lines:
        if '\n' in line:
            lines_treated.append(line.removesuffix('\n'))
        else:
            lines_treated.append(line)

    return lines_treated


def organize_inventories(lines):
    elves = []

    id_elf = 0
    elf = {'name': id_elf, 'calories': 0,}

    for line in lines:
        if line != '':
            elf['calories'] += int(line)
        else:
            elves.append(elf)

            elf = {}
            id_elf += 1
            elf = {'name': id_elf, 'calories': 0,}

        if line == lines[-1]:
            elves.append(elf)
        
    return elves

def most_calories(elves):
    return max(elves, key=lambda el: el['calories'])

with open('./day 1/input', 'r') as input:
    lines = input.readlines()

lines_treated = retiring_n(lines)
elves = organize_inventories(lines_treated)
greedy_elf = most_calories(elves)

print(f"The elf with the greater caloric value is the {greedy_elf['name']} (starting from 0) with {greedy_elf['calories']} calories")