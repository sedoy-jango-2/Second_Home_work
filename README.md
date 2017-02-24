# Second_Home_work
***
Вся домашка разбита на 7 файлов.
***
3 основных файла выполняющих задания
* [get_jobs_data.py](https://github.com/sedoy-jango-2/Second_Home_work/blob/master/get_jobs_data.py)
* [relowed_data_jobs.py](https://github.com/sedoy-jango-2/Second_Home_work/blob/master/relowed_data_jobs.py)
* [get_data_lenguages.py](https://github.com/sedoy-jango-2/Second_Home_work/blob/master/get_data_lenguages.py)
***
и 4 вспомогательных файла содержащих функции
* [get_api.py](https://github.com/sedoy-jango-2/Second_Home_work/blob/master/get_api.py)
* [help_for_get_jobs.py](https://github.com/sedoy-jango-2/Second_Home_work/blob/master/help_for_get_jobs.py)
* [help_for_lenguages.py](https://github.com/sedoy-jango-2/Second_Home_work/blob/master/help_for_lenguages.py)
* [random_colors.py](https://github.com/sedoy-jango-2/Second_Home_work/blob/master/random_colors.py)
***
### h3 заголовок третьего уровня
## h2 Описание действий основных файлов
***
### h3 get_jobs_data.py
При запуске программы выводится сообщение:"Введите город в котором Вы хотите работать: ". Можно ввести название города или его ID, в любом случае она не обвалится. Далее программа запросит ключевые слова для поиска вакансии. Ввод заканчивается после ввода пустой строки. При тестировании рекомендую вводить слова "Программист" и "Разработчик". Далее программа создаст json файл с именем "data_jobs.json", где будет содеражаться информация о 500 вакансиях.
### h3 relowed_data_jobs.py
При запуске программа создат json файл с именем "new_data_jobs.json", где будет содержаться информация указанная в задании 
### h3 get_data_lenguages.py
При запуске программа выдаст список из языков программирования указанных в переменной all_lenguages, где для каждого языка будет выведено количество вакансий после 31 декабря 2016 года со средней зар. платой. также на экране появится график с данными описанными ниже.
## h2 Описание действий вспомогательных файлов
### h3 get_api.py
файл описывающий функцию запроса к api
### h3 help_for_get_jobs.py
файл с функцией создания списка, где признак окончания ввода пустая строка
### h3 ghelp_for_lenguages.py
файл содержащий функции необходимые для выполнения 3-го задания
### h3 random_colors.py
Файл отвечающий за цвета в графике (3-е задание)
