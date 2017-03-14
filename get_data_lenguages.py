import json
import help_for_lenguages
import random_colors

try:
    file_from = open('new_data_jobs.json', encoding='utf-8')
except IOError as e:
    print('Файла не существует\nДля коректной работы запустите get_jobs_data.py')
else:
    print('Исходный файл существует')
    file_from.seek(0)
    data = json.load(file_from)
    all_languages = ['PHP', ' С', '1С', ' C', '1C', 'Java', 'JavaScript', 'Python', 'Delphi', 'C++', 'С++', 'C#', 'Basic', 'Assembler', 'С#', 'F#', 'R', 'Lisp', 'Objective-C', 'Perl', 'Ruby']
    statistic = {}
    for number_of_vacancy in range(len(data)):
        for language_number in range(len(all_languages)):
            help_for_lenguages.count_vacancies(data, statistic, all_languages, number_of_vacancy, language_number)
    graph_dictionary = {}
    help_for_lenguages.print_vacancies(statistic)
    help_for_lenguages.dict_vacancies(statistic, graph_dictionary)
    colors = []
    vacancy_count = 10
    for number_of_vacancy in range(vacancy_count):
        colors.append(random_colors.generate_new_color(colors, pastel_factor=0.8))
    help_for_lenguages.show_vacancies(graph_dictionary, colors)
