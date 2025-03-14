Разработка API на Flask

Домашнее задание

1. Необходимо разработать REST API, предоставляющее возможность ведения блога.

2. API должен иметь минимум 2 сущности:

a. Пользователь
b. Пост
3. Пользователь должен иметь возможность:

a. создать
b. прочитать
c. изменить
d. удалить пост

==========================================Инструкция по запуску======================================================

1. Установить зависимости
    
    pip install -r requirements.txt

2. Запустите приложение

    python app.py

===========================================Примеры запросов==========================================================

1. Создание пользователя

    Метод: POST
    URL: http://localhost:5000/users
    Тело запроса:
    {
        "username": "user1"
    }

2. Создание поста

    Метод: POST
    URL: http://localhost:5000/posts
    Тело запроса:
    {
        "title": "Мой первый пост",
        "content": "Содержимое поста",
        "user_id": 1
    }

3. Получение всех постов

    Метод: GET
    URL: http://localhost:5000/posts

4. Получение одного поста

    Метод: GET
    URL: http://localhost:5000/posts/1

5. Обновление поста

    Метод: PUT
    URL: http://localhost:5000/posts/1
    Тело запроса:
    {
        "title": "Обновленный заголовок",
        "content": "Обновленное содержимое"
    }

6. Удаление поста

    Метод: DELETE
    URL: http://localhost:5000/posts/1