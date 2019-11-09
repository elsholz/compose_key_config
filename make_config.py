import pathlib
from ruamel.yaml import YAML
import sys
import os
from gen_readme.generate_readme import generate_readme
from UnionTrie import UnionTrie
from colorama import ansi

yaml = YAML()


class CollisionCheck:
    def __init__(self):
        self.trie = UnionTrie()

    def collides(self, value, route):
        try:
            self.trie.insert(value, route)
        except UnionTrie.InsertionError as e:
            return True

        return False


collision_check = CollisionCheck()

global_compose_file = open('/usr/share/X11/locale/en_US.UTF-8/Compose')


def extract_key_combos(file_path):
    res = {}
    with open(file_path + '.yaml') as fin:
        r = yaml.load(fin)
    last_title = ''
    collected_lines = []
    # TODO: Collision checking with UnionTries.
    if r:
        for k in r:
            # Check if a new title is being introduced. The lines following after that will belong to that title
            if k == 'title':
                if not last_title == '':
                    res.update({r[k]: collected_lines})
                last_title = r[k]
            # Check of combinations are being specified
            elif k == 'combos':
                for combo in r[k]:
                    collected_lines.append((combo, r[k][combo]))
            elif k == 'include':
                for fp in r[k]:

                    for title, routed_values in extract_key_combos(fp).items():
                        for route, val in routed_values:
                            if not collision_check.collides(val, route):
                                tuple_list = res.get(title, [])
                                tuple_list.append((route, val))
                                res.update({title: tuple_list})
                            else:
                                print(f'{ansi.Fore.RED}Collision!{ansi.Fore.CYAN} The Key Combo'
                                      f' {route} is already mapped to the following character '
                                      f'or sub trie: {str(collision_check.trie[route])}{ansi.Fore.RESET}')
                    # print(res)
                    # res.update(extract_key_combos(fp))
            else:
                if last_title == '':
                    # take last part of path, as filename is used as title is no other title is specified, which
                    # appears to be the case here, because there is no keyword provided previously.
                    # Hence, key combos are written on root level
                    print(last_title)
                    last_title = file_path.split('/')[-1]
                collected_lines.append((k, r[k]))

    if last_title == '':
        last_title = file_path

    if not collected_lines == list():
        res.update({last_title: collected_lines})
    return res


key_combos = extract_key_combos('keys')
conf_lines = []


def global_collision_check(file_content):
    # TODO
    pass


global_collision_check(file_content=global_compose_file.read())

for title, keys in key_combos.items():
    conf_lines.append('# ' + title)
    for (key_combo, output_key) in keys:
        if len(key_combo) == 1:
            # TODO: Check if this works
            conf_line = '<' + '> <'.join(list(key_combo)) + '> : "' + output_key + '" '
        else:
            conf_line = '<Multi_key> <' + '> <'.join(list(key_combo)) + '> : "' + output_key + '" '

        conf_lines.append(conf_line)
    conf_lines.append('')

use_stdout = any(x in sys.argv for x in '--stdout, -s'.split(', '))
gen_rmd = not any(x in sys.argv for x in '--no-readme, -nr'.split(', '))
save_locally = any(x in sys.argv for x in '--save-locally, -sl'.split(', '))


def format_lines(conf_lines):
    comment_lines = [
        '# Config file created with compose_key_config by elsholz',
        '# GitHub: https://github.com/elsholz/compose_key_config',
        ''
    ]

    for comment_line in reversed(comment_lines):
        conf_lines.insert(0, comment_line)
    conf_lines.append('')

    return '\n'.join(conf_lines)


formatted_conf = format_lines(conf_lines)

if use_stdout:
    print(formatted_conf, end='')

else:
    file_dir = str(pathlib.Path.home()) if not save_locally else str(pathlib.Path.cwd())

    with open(os.path.join(file_dir + '/.XCompose'), 'w+') as fout:
        fout.write(formatted_conf)

if gen_rmd:
    generate_readme(key_combos)
