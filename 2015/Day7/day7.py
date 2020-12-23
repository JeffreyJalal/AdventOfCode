import re


f = open("input.txt", "r")
target = "a"
wires = {}
while(target not in wires):
    for line in f:
        operators = re.findall(r'AND|OR|RSHIFT|LSHIFT|NOT|->', line)
        ids = re.findall(r'[a-z]+', line)
        values = re.findall(r'\d+', line)
        values = list(map(lambda val: int(val), values))

        if operators[0] == "->":
            if(len(values) > 0):
                wires[ids[0]] = int(values[0])
            else:
                if(ids[0] in wires):
                    wires[ids[1]] = wires[ids[0]]

        if operators[0] == "NOT":
            if(ids[0] in wires):
                wires[ids[1]] = 2**16 - 1 - wires[ids[0]]

        if operators[0] == "AND":
            if(len(ids) == 3):
                if((ids[0] in wires) & (ids[1] in wires)):
                    wires[ids[2]] = wires[ids[0]] & wires[ids[1]]
            else:
                if(ids[0] in wires):
                    wires[ids[1]] = wires[ids[0]] & values[0]

        if operators[0] == "OR":
            if(len(ids) == 3):
                if((ids[0] in wires) & (ids[1] in wires)):
                    wires[ids[2]] = wires[ids[0]] | wires[ids[1]]
            else:
                if(ids[0] in wires):
                    wires[ids[1]] = wires[ids[0]] | values[0]

        if operators[0] == "LSHIFT":
            if(ids[0] in wires):
                wires[ids[1]] = wires[ids[0]] << values[0]

        if operators[0] == "RSHIFT":
            if(ids[0] in wires):
                wires[ids[1]] = wires[ids[0]] >> values[0]
    print(wires)
    f.seek(0, 0)


print(f'target {target} : {wires[target]}')
