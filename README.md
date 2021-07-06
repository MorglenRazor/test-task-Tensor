<h1>Необходимые компоненты</h1>
    <h3>1.Google Chrome версии 90</h3>
    <h3>2.Python 3.7</h3>
<h2>1. Запустить скачку зависимостей проекта для Linux</h2>

    pip install -r res/requirements

<h2>2. Запустить скачку зависимостей проекта для Windows</h2>
    
    Path/to/python/Scripts/pip.exe install -r requirements.txt
    
<h2>3. Установить дополнительный инструмент для генерации отчетов Allure</h2>

    1. Рассаковать архив allure-commandline-2.10.0.tgz из папки res в новую директорию.

    2. После распаковки перейти в ту директорию и найти папку bin.

    3. Использовать allure.bat for Windows или allure для других Unix платформ.

    4. Добавить allure в системный PATH.
    
    В 3 пунке используеться комманда allure уже установленная в переменую PATH
    Дополнительная информация по устаноке: https://docs.qameta.io/allure/

<h2>3. Перехожим в папку test-automation через терминал или командную строку</h2>
    
    Пишем в терминале или командной строке:
        behave -f allure_behave.formatter:AllureFormatter -o reports/ ./features ; allure serve reports/
