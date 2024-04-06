import os
import re

def append_to_readme(file_path, new_content):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    insertion_index = 7 
    lines = lines[:insertion_index + 1]

    lines.extend(new_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def load_file_name():
    arr = os.listdir('./script/')
    for i in range(len(arr)):
        arr[i] = int(re.sub('.py','',arr[i]))
    arr = sorted(arr)
    text_list = ["### 해결한 수 : `" + str(len(arr)) + "`\n", "\n"]
    for name in arr:
        text_list.append("* [{}](https://github.com/seunggihong/Algorithm/tree/main/script/{}.py)\n".format(name, name))
    return text_list

if __name__ == '__main__':
    readme_path = 'README.md'

    new_content = load_file_name()

    append_to_readme(readme_path, new_content)

