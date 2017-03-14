import requests

def get_jobs_from_sj(town, keywords, api_key):
    keywords = keywords
    url = 'https://api.superjob.ru/2.0/vacancies'
    params = {
        'X-Api-App-Id': api_key
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
    count_of_inquiry = 5
    for i in range(count_of_inquiry):
        jobsData = requests.get(url, headers=params, params=data)
        data['page'] += 1
        vacantion.append(jobsData.json())
    return vacantion
