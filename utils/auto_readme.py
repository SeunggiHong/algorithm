import os

def update_readme():
    with open("./README.md", 'r') as readme:
        readme_content = readme.readlines()

    file_list = [f for f in os.listdir('script') if f.endswith('.py')]

    ex_file_list = set()
    for line in readme_content:
        if line.startswith('- [') and line.endswith('.py)\n'):
            ex_file_list.add(line.strip().split('[', 1)[1].split(']')[0])
    
    new_files = [file_name for file_name in file_list if file_name not in ex_file_list]

    return new_files

if __name__ == "__main__":
    file_list = update_readme()
    if file_list:
        with open("./README.md", 'a') as readme:
            for file_name in file_list:
                readme.write(f'- [{file_name}](https://github.com/seunggihong/Algorithm/tree/main/script/{file_name})\n')