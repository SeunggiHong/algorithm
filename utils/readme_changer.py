import os
import re

scripts = os.listdir('../script/')

sort_script_name = []
for i in scripts:
    sort_script_name.append(int(i[:-3]))

with open('../README.md', 'r', encoding='utf-8') as file:
    readme = file.readlines()
file.close()

readme[9] = '### 해결한 수 : `{}`\n\n'.format(len(scripts))
readme = readme[:11]

for file_name in sorted(sort_script_name):
    readme.append('[{}](https://github.com/seunggihong/Algorithm/tree/main/script/{}.py) \t'.format(file_name, str(file_name) + '.py'))

with open('../README.md', 'w', encoding='utf-8') as file:
    file.writelines(readme)
file.close()
