with open('./keys.yaml', 'r') as fin:
    lines_filtered = []
    for line in fin.readlines():
        if not line.isspace():
            lines_filtered.append(line[:-1])

# print(*lines_filtered, sep='\n')

letter_combinations = None
titles = {}

for lf in lines_filtered:
    if lf[0] == '#':
        # titles.append(lf[2:])
        titles[lf[2:]] = {}
        letter_combinations = titles[lf[2:]]
    else:
        k, v = lf.split(':')
        letter_combinations[k] = v.lstrip()
# print(letter_combinations)
print('titles:', titles)

print('#### List of default compose key combinations added by compose_key_config:')

with open('./readme.md', 'w') as readme, open('./readme_base.md') as readme_base:
    readme.write(readme_base.read())
    readme.write('\n')
    for title, letter_combs in titles.items():
        readme.write('##### ' + title + '\n')
        readme.write('|Combination|Result|\n|---|---|\n')

        for comb, ltr in letter_combs.items():
            readme.write('| \<' + '\> \<'.join(list(comb)) + '\> | ' + ltr + ' | \n')

    readme.write('\n')
