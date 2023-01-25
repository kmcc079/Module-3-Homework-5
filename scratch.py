import re
f = open('names.txt')
data = f.readlines()
# print(data)

full_name_patt = re.compile('(^[A-Za-z]+), ([A-Za-z]+-[A-Za-z]+|[A-Za-z]+)')
handle_patt = re.compile('@[a-z]+$')

for line in data:
    if re.search('@[a-z]+$', line):
        # print(line)
        name = full_name_patt.search(line)
        handle = handle_patt.search(line)
        if name:
            name.groups()
            name.group(1)
            name.group(2)
        if handle:
            handle.group()
        print(f'{name.group(2)} {name.group(1)} / {handle.group()}\n')