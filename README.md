<h1>Необходимые компоненты</h1>
    <h3>1.Google Chrome версии 90</h3>
    <h3>2.Python 3.7</h3>
<h2>1. Запустить скачку зависимостей проекта для Linux</h2>

    pip install -r res/requirements

<h2>2. Запустить скачку зависимостей проекта для Windows</h2>
    
    Path/to/python/Scripts/pip.exe install -r requirements.txt

<h2>3. Перехожим в папку test-automation через терминал или командную строку</h2>
    
    Пишем в терминале или командной строке:
        для запуска первого теста:
            behave -i features/search_in_yandex.feature
        для запуска второго теста:
            behave -i features/pictures_on_yandex.feature
