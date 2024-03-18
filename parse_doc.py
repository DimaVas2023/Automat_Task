from doc_info import DocInfo as di
import functions as fun


solutions, works = fun.parse_file('9_File_judical.txt')

for i in solutions:
    solution_info = i.split('window.Ya.adfoxCode.create({')[0]
    number = solution_info.split(' от')[0]
    date = solution_info.split('от ')[-1].split(' по делу №')[0]
    place_number = solution_info.split(f'по делу № ')[-1].split('   - ')[0]
    space = place_number.index(' ')
    place = place_number[space:]

    di.solution_numbers.append(number)
    di.solution_dates.append(date)
    di.solution_places.append(place)

for i in works:
    court = i.split('Судьи дела:')[1].strip()
    di.courts.append(court)
    try:
        numb = i.lstrip()
        space = numb.index(' ')
        int(numb[0])
        int(numb[:space][-4])
        di.work_numbers.append(numb[:space])
    except:
        with open('view.txt', 'a', encoding='utf-8') as f: # Сделал файл в который заносятся решения которые не удалось спарсить
            f.write(numb+'\n')


print(f'\nНомера решений:\n{di.solution_numbers}')
print(f'\nДаты принятия решений:\n{di.solution_dates}')
print(f'\nНомера дел:\n{di.work_numbers}')
print(f'\nМеста принятия решений:\n{di.solution_places}')
print(f'\nСудьи:\n{di.courts}')
