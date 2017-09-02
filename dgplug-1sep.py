#!/usr/bin/env python3
def module_search(file):
    with open(file,'r' ) as fobj:
        all_modules = []
        for line in fobj:
            data = line.split()
            for item in data:
                if item=="from":
                    all_modules.append(data[data.index(item)+1])
    return all_modules 

print("the imported modules in list form ",module_search("1.py"))
