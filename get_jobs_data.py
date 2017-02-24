import get_api
import json
import help_for_get_jobs


city = input('Введите город в котором Вы хотите работать: ')
print('Введите ключевые слова')
keywords = []
help_for_get_jobs.input_keywords(keywords)
print('Запись началась')
vocation = get_api.getApiFromSj(city, keywords=keywords)
with open('data_jobs.json', 'w', encoding='utf-8') as outfile:
    json.dump(vocation, outfile, sort_keys=True, indent=4, ensure_ascii=False)
outfile.close()
print('Запись закончена')
