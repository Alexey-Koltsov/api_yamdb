#Описание проекта «YaMDb»

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Добавлять произведения, категории и жанры может только администратор. Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв. Пользователи могут оставлять комментарии к отзывам. Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

#Стек использованных технологий

Python3
Django Framework
Django Rest Framework
Postman
SQLite3
#Как запустить проект

##Клонировать репозиторий и перейти в него в командной строке

git clone git@github.com:Alexey-Koltsov/api_yamdb.git
cd api_yamdb
##Cоздать виртуальное окружение

Windows

python -m venv venv
##Активировать виртуальное окружение Windows

source venv/Scripts/activate
LinuxmacOS

python3 -m venv venv source venvbinactivate
##Обновить PIP

Windows

python -m pip install --upgrade pip
LinuxmacOS

python3 -m pip install --upgrade pip
##Установить зависимости из файла requirements.txt

pip install -r requirements.txt
##Выполнить миграции

Windows

python manage.py makemigrations
python manage.py migrate
LinuxmacOS

python3 manage.py makemigrations
python3 manage.py migrate
##Запустить проект

Windows

python manage.py runserver
LinuxmacOS

python3 manage.py runserver
#База данных

Тестировать пустой проект неудобно, а наполнять его руками — долго. В репозитории с заданием, в директории /api_yamdb/static/data, подготовлены несколько файлов в формате csv с контентом для ресурсов Users, Titles, Categories, Genres, Reviews и Comments. После того, как вы подготовите модели, заполните базу данных контентом из приложенных csv-файлов. Перейдите в папку с manage.py и менеджмент командой cделайте импорт в БД.

python manage.py import_data
#AUTH Регистрация пользователей и выдача токенов

##Регистрация нового пользователя

Получить код подтверждения на переданный email. Права доступа: Доступно без токена. Использовать имя 'me' в качестве username запрещено. Поля email и username должны быть уникальными. Должна быть возможность повторного запроса кода подтверждения.

POST /auth/signup/

{
  "email": "user@example.com",
  "username": "string"
}
Пример ответа:

{
  "email": "string",
  "username": "string"
}
##Получение JWT-токена

Получение JWT-токена в обмен на username и confirmation code. Права доступа: Доступно без токена.

POST /auth/token/
{
  "username": "string",
  "confirmation_code": "string"
}
Пример ответа:

{
  "token": "string"
}
#CATEGORIES

##Категории (типы) произведений

Получение списка всех категорий

Получить список всех категорий Права доступа: Доступно без токена

GET categories/
Пример ответа

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "name": "string",
      "slug": "string"
    }
  ]
}
##Добавление новой категории

Создать категорию. Права доступа: Администратор. Поле slug каждой категории должно быть уникальным.

POST categories/
{
  "name": "string",
  "slug": "string"
}
Пример ответа:

{
  "name": "string",
  "slug": "string"
}
##Удаление категории

Удалить категорию. Права доступа: Администратор.

DELETE categories/{slug}/
#GENRES

#Категории жанров

##Получение списка всех жанров

Получить список всех жанров. Права доступа: Доступно без токена

GET genres/
Пример ответа:

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "name": "string",
      "slug": "string"
    }
  ]
}
##Добавление жанра

Добавить жанр. Права доступа: Администратор. Поле slug каждого жанра должно быть уникальным.

http://127.0.0.1:8000/api/v1/genres/
{
  "name": "string",
  "slug": "string"
}
Пример ответа:

{
  "name": "string",
  "slug": "string"
}
##Удаление жанра

Удалить жанр. Права доступа: Администратор.

DELETE genres/{slug}/
#TITLES

Произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

##Получение списка всех произведений

Получить список всех объектов. Права доступа: Доступно без токена

GET titles/
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
##Добавление произведения

Добавить новое произведение. Права доступа: Администратор. Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего). При добавлении нового произведения требуется указать уже существующие категорию и жанр.

POST /titles/
Пример запроса:

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
Пример ответа:

{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
##Получение информации о произведении

Информация о произведении Права доступа: Доступно без токена

GET titles/{titles_id}/
Пример ответа:

{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
##Частичное обновление информации о произведении

Обновить информацию о произведении Права доступа: Администратор

PATCH titles/{titles_id}/
Пример запроса:

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
Пример ответа:

{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
##Удаление произведения

Удалить произведение. Права доступа: Администратор.

DELETE titles/{titles_id}/
#REVIEWS

#Отзывы

##Получение списка всех отзывов

Получить список всех отзывов. Права доступа: Доступно без токена.

GET titles/{title_id}/reviews/
Пример ответа:

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "text": "string",
      "author": "string",
      "score": 1,
      "pub_date": "2019-08-24T14:15:22Z"
    }
  ]
}
##Добавление нового отзыва

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение. Права доступа: Аутентифицированные пользователи.

POST titles/{title_id}/reviews/
Пример запроса:

{
  "text": "string",
  "score": 1
}
Пример ответа:

{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
##Получение отзыва по id

Получить отзыв по id для указанного произведения. Права доступа: Доступно без токена

GET titles/{title_id}/reviews/{review_id}/
Пример ответа:

{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
##Частичное обновление отзыва по id

Частично обновить отзыв по id. Права доступа: Автор отзыва, модератор или администратор.

PATCH titles/{title_id}/reviews/{review_id}/
Пример запроса:

{
  "text": "string",
  "score": 1
}
Пример ответа:

{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
##Удаление отзыва по id

Удалить отзыв по id Права доступа: Автор отзыва, модератор или администратор.

DELETE titles/{title_id}/reviews/{review_id}/
#COMMENTS

##Комментарии к отзывам

Получение списка всех комментариев к отзыву

Получить список всех комментариев к отзыву по id Права доступа: Доступно без токена.

GET titles/{title_id}/reviews/{review_id}/comments/
Пример ответа:

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "text": "string",
      "author": "string",
      "pub_date": "2019-08-24T14:15:22Z"
    }
  ]
}
##Добавление комментария к отзыву

Добавить новый комментарий для отзыва. Права доступа: Аутентифицированные пользователи.

GET titles/{title_id}/reviews/{review_id}/comments/
Пример запроса:

{
  "text": "string"
}
Пример ответа:

{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
##Получение комментария к отзыву

Получить комментарий для отзыва по id. Права доступа: Доступно без токена.

GET titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
Пример ответа:

{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
##Частичное обновление комментария к отзыву

Частично обновить комментарий к отзыву по id. Права доступа: Автор комментария, модератор или администратор.

PATCH titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
Пример запроса:

{
  "text": "string"
}
Пример ответа:

{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
#Удаление комментария к отзыву

Удалить комментарий к отзыву по id. Права доступа: Автор комментария, модератор или администратор.

DELETE titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
#USERS

#Пользователи

##Получение списка всех пользователей

Получить список всех пользователей. Права доступа: Администратор

GET /users/
Пример ответа:

{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "username": "string",
      "email": "user@example.com",
      "first_name": "string",
      "last_name": "string",
      "bio": "string",
      "role": "user"
    }
  ]
}
##Добавление пользователя

Добавить нового пользователя. Права доступа: Администратор Поля email и username должны быть уникальными.

POST /users/
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
Пример ответа:

{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
##Получение пользователя по username

Получить пользователя по username. Права доступа: Администратор

GET /users/{username}/ Пример ответа:

{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
##Изменение данных пользователя по username

Изменить данные пользователя по username. Права доступа: Администратор. Поля email и username должны быть уникальными.

PATCH /users/{username}/

{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
Пример ответа:

{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
##Удаление пользователя по username

Удалить пользователя по username. Права доступа: Администратор.

DELETE /users/{username}/

##Получение данных своей учетной записи

Получить данные своей учетной записи Права доступа: Любой авторизованный пользователь

GET /users/me/ Пример ответа:

{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
##Изменение данных своей учетной записи

Изменить данные своей учетной записи Права доступа: Любой авторизованный пользователь Поля email и username должны быть уникальными.

PATCH /users/me/

{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string"
}
Пример ответа:

{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
#Авторы: Лозинская Елизавета, Охрим Павел, Кольцов Алексей.