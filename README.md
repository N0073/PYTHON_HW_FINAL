Провести автоматизированное тестирование UI и API-тестов для сайта "Деливери"
Задача проекта
Провести автоматизированное тестирование UI и API-тестов для сайта "Деливери".

Шаблон для автоматизации тестирования на python
Шаги
Склонировать проект 'git clone'
Стек
pytest
селен
Запрос
Привлекательность
Запуск тестов:
Pytest # все тесты
pytest -m ui # только UI-тесты
pytest -m API # только API-тесты
Структура
test_api - тесты АПИ
test_ui - тесты UI
Библиотеки
PIP Install pyTest
Pip Install Selenium
pip install webdriver-manager
PIP Install Allure
Ссылка на финальный проект:

# Установка зависимостей
pip install pytest allure-pytest requests

# Запуск тестов
pytest test_cart.py --alluredir=./allure-results

# Генерация отчета
allure serve ./allure-results