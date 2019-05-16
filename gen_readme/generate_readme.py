def generate_readme(conf):
    with open('./README.md', 'w') as readme:
        with open('./gen_readme/readme_base.md') as readme_base, open('./gen_readme/readme_end.md') as readme_end:
            rmd_base = readme_base.read()
            rmd_end = readme_end.read()

        readme.write(rmd_base + '\n')

        for title, keys in conf.items():
            readme.write('### ' + title + '\n')
            readme.write('|Combination|Result|\n|---|---|\n')

            for comb, ltr in keys:
                readme.write('| \<' + '\> \<'.join(list(comb)) + '\> | ' + ltr + ' | \n')
            readme.write('\n')

        readme.write((rmd_end + '\n'))
