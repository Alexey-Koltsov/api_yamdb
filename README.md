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