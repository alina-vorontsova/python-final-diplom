[Описание проекта](../README.md)

Запуск проекта: 

1. Создать виртуальное окружение, установить зависимости, при необходимости поменять значения в `orders/.env`
2. Создать базу данных 
```bash
createdb -U postgres diploma
```
3. Провести миграции 
```bash
python orders/manage.py makemigrations
python orders/manage.py migrate
```
4. Запустить сервер 
```bash 
python orders/manage.py runserver
```
5. Посылать запросы на сервер можно через [postman-collection](../postman_collection.json)