import requests

def getApiFromSj(town, keywords):
    keywords = keywords
    url = 'https://api.superjob.ru/2.0/vacancies'
    params = {
        'X-Api-App-Id': 'ключ api'
    }
    data = {
        'town': town,
        'keyword': keywords,
        'catalogues': 48,
        'date_published_from': 1480550400,
        'page': 1,
        'count': 100,
    }
    vacantion = []
    for i in range(5):
        jobsData = requests.get(url, headers=params, params=data)
        data['page'] += 1
        vacantion.append(jobsData.json())
    return vacantion
