## API для социальной сети Yatube
В API реализованы следующие возможности:
- получить, обновить токен авторизации JWT;
- публиковать и удалять свои записи;
- комментировать записи, изменять или удалять свои комметнарии к записи;
- получить список подписок, а также подписываться от авторов.

## Технологии
Python 3.7, Django 3.2, DRF, JWT + Djoser

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:bolognesespaghetti/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать виртуальное окружение:

```
python3 -m venv env
```
Активировать виртульное окружение

    source env/bin/activate

Обновить pip

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
