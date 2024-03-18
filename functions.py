import re


def parse_file(filename: str):
    '''Принимает имя файла и выдаёт его решения и дела'''
    solution = []
    work = []
    with open(filename, 'r', encoding='utf-8') as f:
        file = f.read()
        solution = re.split("  Решение № ", file, flags=re.IGNORECASE)[1:]#file.split('  Решение № ')[1:]   
        work_trash = re.split("Дело №", file, flags=re.IGNORECASE)[1:]
        for i in work_trash:
            if '(судья)' in i:
                j = i.index('(судья)')
                work.append(i[:j+10])
                
    return solution, work