from collections import Counter
with open("input.txt") as f:
    l = [x.strip("\n").split("|") for x in f]

keys = ['a','b','c','d','e','f','g']
ideal_map = {'1':"cf",'2':"acdeg",'3':"acdfg",'4':"bcdf",'5':"abdfg",'6':"abdefg",'7':"acf",'8':"abcdefg",'9':"abcdfg",'0':"abcefg"}
ideal_map = {k:v for v,k in ideal_map.items()}
d = {1:0,4:0,7:0,8:0}


def SolveUniques(inp):
    uniques = {2:"",4:"",3:"",7:""}
    for x in inp:
        if not len(x) == 5 and not len(x) == 6:
            uniques[len(x)] = x
    return uniques

def getMapping(inp,mapping):
    uniques = SolveUniques(inp)
    for c in uniques[3]:
        if not c in uniques[2]:
            mapping['a'] = c
            break
    
    bd = []
    for c in uniques[4]:
        if not c in uniques[2]:
            bd.append(c)

    eg = []
    for c in uniques[7]:
        if c not in set(uniques[3]+uniques[4]+uniques[2]):
            eg.append(c)
    return RulesApplication(inp,mapping,uniques,bd,eg)

def RulesApplication(inp,mapping,uniques,bd,eg):
    sixes = [x for x in inp if len(x) == 6]
    c = Counter("".join(sixes))
    afbg = [x for x,y in c.items() if y == 3]
    cde = [x for x,y in c.items() if y == 2]
    if bd[0] in afbg:
        mapping['b'] = bd[0]
        mapping['d'] = bd[1]
    else:
        mapping['b'] = bd[1]
        mapping['d'] = bd[0]
    if uniques[2][0] in afbg:
        mapping['f'] = uniques[2][0]
        mapping['c'] = uniques[2][1]
    else:
        mapping['f'] = uniques[2][1]
        mapping['c'] = uniques[2][0]
    for c in afbg:
        if c not in mapping.values():
            mapping['g'] = c
    if eg[0] == mapping['g']:
        mapping['e'] = eg[1]
    else:
        mapping['e'] = eg[0]
    for c in cde:
        if not c in mapping.values():
            mapping['c'] = c
    return mapping

s = 0
for inp,out in l:
    inp = inp.strip(" ").split(" ")
    mapping = getMapping(inp, {x:'_' for x in keys})
    out = out.strip(" ").split(" ")
    revmapping = {v:k for k,v in mapping.items()}
    numbers = ""
    for outseg in out:
        noutseg = ""
        for c in outseg:
            noutseg+=revmapping[c]
        numbers+=ideal_map["".join(sorted(noutseg))]
    s+=int(numbers)
    
