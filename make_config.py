import pathlib
import yaml
import sys

with open('keys.yaml', 'r') as fin:
    root = yaml.safe_load(fin)
    conf_lines = []
    for key_combo in root:
        output_key = root[key_combo]
        try:
            assert len(key_combo) > 0

            if len(key_combo) == 1:
                conf_line = '<' + '> <'.join(list(key_combo)) + '> : "' + output_key + '" '
            else:
                conf_line = '<Multi_key> <' + '> <'.join(list(key_combo)) + '> : "' + output_key + '" '

            conf_lines.append(conf_line)

        except AssertionError as e:
            print('Assertion error')

if '-s' in sys.argv or '--stdout' in sys.argv:
    print('\n'.join(conf_lines))
else:
    with open(str(pathlib.Path.home()) + '/.XCompose', 'w+') as fout:
        comment_lines = [
            '# Config file created with compose_key_config by elsholz',
            '# GitHub: https://github.com/elsholz/compose_key_config.git',
            ''
        ]

        for comment_line in reversed(comment_lines):
            conf_lines.insert(0, comment_line)
        conf_lines.append('')
        fout.write('\n'.join(conf_lines))
