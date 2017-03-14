import get_api
import json
import help_for_get_jobs


city = input('Введите город в котором Вы хотите работать: ')
print('Введите ключевые слова')
keywords = []
help_for_get_jobs.input_keywords()
api_key = input('Введите ключ API')
print('Запись началась')
vocation = get_api.get_jobs_from_sj(city, keywords=keywords, api_key=api_key)
with open('data_jobs.json', 'w', encoding='utf-8') as outfile:
    json.dump(vocation, outfile, sort_keys=True, indent=4, ensure_ascii=False)
outfile.close()
print('Запись закончена')
