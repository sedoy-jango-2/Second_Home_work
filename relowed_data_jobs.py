import json

try:
    file_from = open('data_jobs.json', encoding='utf-8')
except IOError as e:
    print('Файла не существует\nДля коректной работы запустите get_jobs_data.py')
else:
    print('Исходный файл существует')
    file_from.seek(0)
    data = json.load(file_from)
    all_vacancy = []
    for j in range(len(data)):
        for i in range(len(data[j]['objects'])):
            tmp_vacancy = {
                        "profession": data[j]["objects"][i]["profession"],
                        "payment_from": data[j]["objects"][i]["payment_from"],
                        "payment_to": data[j]["objects"][i]["payment_to"],
                        "candidat": data[j]["objects"][i]["candidat"]
                    }
            all_vacancy.append(tmp_vacancy)
with open('new_data_jobs.json', 'w', encoding='utf-8') as outfile:
    json.dump(all_vacancy, outfile, sort_keys=True, indent=4, ensure_ascii=False)