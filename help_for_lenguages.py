import matplotlib.pyplot as plt
import numpy as np
import random_colors

def count_vacancies(data, statistic, all_lenguages, i, j):
    if data[i]["candidat"] != None:
        if data[i]["candidat"].find(all_lenguages[j]) != -1 or data[i]["profession"].find(all_lenguages[j]) != -1:
            flag = False
            for key, value in statistic.items():
                if all_lenguages[j] == key:
                    flag = True
            if not flag:
                statistic[all_lenguages[j]] = {}
                statistic[all_lenguages[j]]['quantity'] = 0
                statistic[all_lenguages[j]]['money'] = 0
                statistic[all_lenguages[j]]['payment_quantity'] = 0
                if data[i]['payment_from'] > 0 and data[i]['payment_to']:
                    statistic[all_lenguages[j]]['money'] = (data[i]['payment_from'] + data[i]['payment_to']) // 2
                    statistic[all_lenguages[j]]['payment_quantity'] = 1
                elif data[i]['payment_from'] > 0 or data[i]['payment_to']:
                    statistic[all_lenguages[j]]['money'] = max(data[i]['payment_from'], data[i]['payment_to'])
                    statistic[all_lenguages[j]]['payment_quantity'] = 1
                statistic[all_lenguages[j]]['quantity'] = 1
            else:
                if data[i]['payment_from'] > 0 and data[i]['payment_to']:
                    statistic[all_lenguages[j]]['money'] += (data[i]['payment_from'] + data[i]['payment_to']) // 2
                    statistic[all_lenguages[j]]['payment_quantity'] += 1
                elif data[i]['payment_from'] > 0 or data[i]['payment_to']:
                    statistic[all_lenguages[j]]['money'] += max(data[i]['payment_from'], data[i]['payment_to'])
                    statistic[all_lenguages[j]]['payment_quantity'] += 1
                statistic[all_lenguages[j]]['quantity'] += 1
            return statistic

def sum_params(dict, eng_parametr, rus_parametr):
    dict[eng_parametr]['quantity'] += dict[rus_parametr]['quantity']
    dict[eng_parametr]['money'] += dict[rus_parametr]['money']
    dict[eng_parametr]['payment_quantity'] += dict[rus_parametr]['payment_quantity']
    del dict[rus_parametr]
    return dict

def print_vacancies(statistic):
    sum_params(statistic, ' C', ' С')
    sum_params(statistic, 'C++', 'С++')
    sum_params(statistic, '1C', '1С')
    sum_params(statistic, 'C#', 'С#')
    for key, value in statistic.items():
        print(key)
        print('Количество вакансий: ', value['quantity'])
        if value['payment_quantity'] != 0:
            print('Средняя заработная плата: ', value['money']//value['payment_quantity'])
    return 0

def dict_vacancies(statistic, dict):
    for key, value in statistic.items():
        if value['payment_quantity'] != 0:
            dict[key] = value['money'] // value['payment_quantity']
    return dict

def show_vacancies(graphDict, colors):
    name_graph = []
    salary_graph = []
    for key in graphDict.keys():
        if graphDict[key] != 0:
            name_graph.append(key)
            salary_graph.append(graphDict[key])
    X = salary_graph
    Y = np.arange(len(X))
    L = name_graph
    for i in plt.bar(Y, X, align='center'):
        i.set_color(random_colors.random.choice(colors))
    plt.xticks(Y, L)
    plt.title('Статистика по зарплатам')
    plt.ylabel('Средняя зарплата в рублях')
    plt.xlabel('Языки программирования')
    plt.show()
    return 0