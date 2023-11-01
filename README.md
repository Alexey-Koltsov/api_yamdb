#Описание проекта «YaMDb»

<<<<<<< HEAD
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
=======
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

#Стек использованных технологий

- Python3
- Django Framework
- Django Rest Framework
- Postman
- SQLite3

#Как запустить проект

##Клонировать репозиторий и перейти в него в командной строке
```
git clone git@github.com:Alexey-Koltsov/api_yamdb.git
```
```
cd api_yamdb
```
##Cоздать виртуальное окружение

Windows
```
python -m venv venv
```
##Активировать виртуальное окружение Windows
```
source venv/Scripts/activate
```
LinuxmacOS
```
python3 -m venv venv source venvbinactivate
```
##Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
LinuxmacOS
```
python3 -m pip install --upgrade pip
```
##Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
##Выполнить миграции

Windows
```
python manage.py makemigrations
```
```
python manage.py migrate
```
LinuxmacOS
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
##Запустить проект

Windows
```
python manage.py runserver
```
LinuxmacOS
```
python3 manage.py runserver
```

#База данных

Тестировать пустой проект неудобно, а наполнять его руками — долго. 
В репозитории с заданием, в директории /api_yamdb/static/data, подготовлены несколько файлов в формате csv с контентом для ресурсов Users, Titles, Categories, Genres, Reviews и Comments. 
После того, как вы подготовите модели, заполните базу данных контентом из приложенных csv-файлов. 
Перейдите в папку с manage.py и менеджмент командой cделайте импорт в БД.
```
python manage.py import_data
```

#AUTH
Регистрация пользователей и выдача токенов
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed

##Регистрация нового пользователя

Получить код подтверждения на переданный email. Права доступа: Доступно без токена. Использовать имя 'me' в качестве username запрещено. Поля email и username должны быть уникальными. Должна быть возможность повторного запроса кода подтверждения.

POST /auth/signup/
<<<<<<< HEAD

=======
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "email": "user@example.com",
  "username": "string"
}
<<<<<<< HEAD
Пример ответа:

=======
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "email": "string",
  "username": "string"
}
<<<<<<< HEAD
=======
```


>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
##Получение JWT-токена

Получение JWT-токена в обмен на username и confirmation code. Права доступа: Доступно без токена.

<<<<<<< HEAD
POST /auth/token/
=======
```
POST /auth/token/
```
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "confirmation_code": "string"
}
<<<<<<< HEAD
Пример ответа:

{
  "token": "string"
}
=======
```
Пример ответа:
```
{
  "token": "string"
}
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
#CATEGORIES

##Категории (типы) произведений

Получение списка всех категорий

Получить список всех категорий Права доступа: Доступно без токена
<<<<<<< HEAD

GET categories/
Пример ответа

=======
```
GET categories/
```
Пример ответа
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
##Добавление новой категории

Создать категорию. Права доступа: Администратор. Поле slug каждой категории должно быть уникальным.

POST categories/
=======
```

##Добавление новой категории

Создать категорию. Права доступа: Администратор. Поле slug каждой категории должно быть уникальным.
```
POST categories/
```
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "name": "string",
  "slug": "string"
}
<<<<<<< HEAD
Пример ответа:

=======
```

Пример ответа:

```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "name": "string",
  "slug": "string"
}
<<<<<<< HEAD
##Удаление категории

Удалить категорию. Права доступа: Администратор.

DELETE categories/{slug}/
=======
```


##Удаление категории

Удалить категорию. Права доступа: Администратор.
```
DELETE categories/{slug}/
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
#GENRES

#Категории жанров

##Получение списка всех жанров

Получить список всех жанров. Права доступа: Доступно без токена
<<<<<<< HEAD

GET genres/
Пример ответа:

=======
```
GET genres/
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
##Добавление жанра

Добавить жанр. Права доступа: Администратор. Поле slug каждого жанра должно быть уникальным.

http://127.0.0.1:8000/api/v1/genres/
=======
```

##Добавление жанра

Добавить жанр. Права доступа: Администратор. Поле slug каждого жанра должно быть уникальным.
```
http://127.0.0.1:8000/api/v1/genres/
```
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "name": "string",
  "slug": "string"
}
<<<<<<< HEAD
Пример ответа:

=======
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "name": "string",
  "slug": "string"
}
<<<<<<< HEAD
##Удаление жанра

Удалить жанр. Права доступа: Администратор.

DELETE genres/{slug}/
=======
```

##Удаление жанра

Удалить жанр. Права доступа: Администратор.
```
DELETE genres/{slug}/
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
#TITLES

Произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

##Получение списка всех произведений

Получить список всех объектов. Права доступа: Доступно без токена
<<<<<<< HEAD

GET titles/
=======
```
GET titles/
```
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
##Добавление произведения

Добавить новое произведение. Права доступа: Администратор. Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего). При добавлении нового произведения требуется указать уже существующие категорию и жанр.

POST /titles/
Пример запроса:

=======
```

##Добавление произведения

Добавить новое произведение. Права доступа: Администратор. 
Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего). 
При добавлении нового произведения требуется указать уже существующие категорию и жанр.
```
POST /titles/
```
Пример запроса:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
<<<<<<< HEAD
Пример ответа:

=======
```

Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
=======
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
##Получение информации о произведении

Информация о произведении Права доступа: Доступно без токена

<<<<<<< HEAD
GET titles/{titles_id}/
Пример ответа:

=======
```
GET titles/{titles_id}/
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
##Частичное обновление информации о произведении

Обновить информацию о произведении Права доступа: Администратор

PATCH titles/{titles_id}/
Пример запроса:

=======
```

##Частичное обновление информации о произведении

Обновить информацию о произведении Права доступа: Администратор
```
PATCH titles/{titles_id}/
```
Пример запроса:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
<<<<<<< HEAD
Пример ответа:

=======
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
##Удаление произведения

Удалить произведение. Права доступа: Администратор.

DELETE titles/{titles_id}/
=======
```

##Удаление произведения

Удалить произведение. Права доступа: Администратор.
```
DELETE titles/{titles_id}/
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
#REVIEWS

#Отзывы

##Получение списка всех отзывов

Получить список всех отзывов. Права доступа: Доступно без токена.
<<<<<<< HEAD

GET titles/{title_id}/reviews/
Пример ответа:

=======
```
GET titles/{title_id}/reviews/
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
##Добавление нового отзыва

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение. Права доступа: Аутентифицированные пользователи.

POST titles/{title_id}/reviews/
Пример запроса:

=======
```

##Добавление нового отзыва

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение. Права доступа: Аутентифицированные пользователи.
```
POST titles/{title_id}/reviews/
```
Пример запроса:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "text": "string",
  "score": 1
}
<<<<<<< HEAD
Пример ответа:

=======
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
<<<<<<< HEAD
##Получение отзыва по id

Получить отзыв по id для указанного произведения. Права доступа: Доступно без токена

GET titles/{title_id}/reviews/{review_id}/
Пример ответа:

=======
```

##Получение отзыва по id

Получить отзыв по id для указанного произведения. Права доступа: Доступно без токена
```
GET titles/{title_id}/reviews/{review_id}/
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
<<<<<<< HEAD
##Частичное обновление отзыва по id

Частично обновить отзыв по id. Права доступа: Автор отзыва, модератор или администратор.

PATCH titles/{title_id}/reviews/{review_id}/
Пример запроса:

=======
```

##Частичное обновление отзыва по id

Частично обновить отзыв по id. Права доступа: Автор отзыва, модератор или администратор.
```
PATCH titles/{title_id}/reviews/{review_id}/
```
Пример запроса:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "text": "string",
  "score": 1
}
<<<<<<< HEAD
Пример ответа:

=======
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
<<<<<<< HEAD
##Удаление отзыва по id

Удалить отзыв по id Права доступа: Автор отзыва, модератор или администратор.

DELETE titles/{title_id}/reviews/{review_id}/
=======
```

##Удаление отзыва по id

Удалить отзыв по id Права доступа: Автор отзыва, модератор или администратор.
```
DELETE titles/{title_id}/reviews/{review_id}/
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
#COMMENTS

##Комментарии к отзывам

Получение списка всех комментариев к отзыву

Получить список всех комментариев к отзыву по id Права доступа: Доступно без токена.
<<<<<<< HEAD

GET titles/{title_id}/reviews/{review_id}/comments/
Пример ответа:

=======
```
GET titles/{title_id}/reviews/{review_id}/comments/
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
##Добавление комментария к отзыву

Добавить новый комментарий для отзыва. Права доступа: Аутентифицированные пользователи.

GET titles/{title_id}/reviews/{review_id}/comments/
Пример запроса:

{
  "text": "string"
}
Пример ответа:

=======
```

##Добавление комментария к отзыву

Добавить новый комментарий для отзыва. Права доступа: Аутентифицированные пользователи.
```
GET titles/{title_id}/reviews/{review_id}/comments/
```
Пример запроса:
```
{
  "text": "string"
}
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
<<<<<<< HEAD
##Получение комментария к отзыву

Получить комментарий для отзыва по id. Права доступа: Доступно без токена.

GET titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
Пример ответа:

=======
```

##Получение комментария к отзыву

Получить комментарий для отзыва по id. Права доступа: Доступно без токена.
```
GET titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
<<<<<<< HEAD
##Частичное обновление комментария к отзыву

Частично обновить комментарий к отзыву по id. Права доступа: Автор комментария, модератор или администратор.

PATCH titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
Пример запроса:

{
  "text": "string"
}
Пример ответа:

=======
```

##Частичное обновление комментария к отзыву

Частично обновить комментарий к отзыву по id. Права доступа: Автор комментария, модератор или администратор.
```
PATCH titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
Пример запроса:
```
{
  "text": "string"
}
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
<<<<<<< HEAD
#Удаление комментария к отзыву

Удалить комментарий к отзыву по id. Права доступа: Автор комментария, модератор или администратор.

DELETE titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
=======
```

#Удаление комментария к отзыву

Удалить комментарий к отзыву по id. Права доступа: Автор комментария, модератор или администратор.
```
DELETE titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
#USERS

#Пользователи

##Получение списка всех пользователей

Получить список всех пользователей. Права доступа: Администратор
<<<<<<< HEAD

GET /users/
Пример ответа:

=======
```
GET /users/
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
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
<<<<<<< HEAD
##Добавление пользователя

Добавить нового пользователя. Права доступа: Администратор Поля email и username должны быть уникальными.

POST /users/
=======
```

##Добавление пользователя

Добавить нового пользователя. Права доступа: Администратор Поля email и username должны быть уникальными.
```
POST /users/
```
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
<<<<<<< HEAD
Пример ответа:

=======
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
<<<<<<< HEAD
=======
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
##Получение пользователя по username

Получить пользователя по username. Права доступа: Администратор

<<<<<<< HEAD
GET /users/{username}/ Пример ответа:

=======
GET /users/{username}/
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
<<<<<<< HEAD
=======
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
##Изменение данных пользователя по username

Изменить данные пользователя по username. Права доступа: Администратор. Поля email и username должны быть уникальными.

PATCH /users/{username}/
<<<<<<< HEAD

=======
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
<<<<<<< HEAD
Пример ответа:

=======
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
<<<<<<< HEAD
=======
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
##Удаление пользователя по username

Удалить пользователя по username. Права доступа: Администратор.

DELETE /users/{username}/

##Получение данных своей учетной записи

Получить данные своей учетной записи Права доступа: Любой авторизованный пользователь

<<<<<<< HEAD
GET /users/me/ Пример ответа:

=======
GET /users/me/
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
<<<<<<< HEAD
=======
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
##Изменение данных своей учетной записи

Изменить данные своей учетной записи Права доступа: Любой авторизованный пользователь Поля email и username должны быть уникальными.

PATCH /users/me/
<<<<<<< HEAD

=======
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string"
}
<<<<<<< HEAD
Пример ответа:

=======
```
Пример ответа:
```
>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
<<<<<<< HEAD
=======
```

>>>>>>> 39fa275f2ec943f5cf022eced3f9acccb5022aed
#Авторы: Лозинская Елизавета, Охрим Павел, Кольцов Алексей.