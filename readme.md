# Пульт охраны банка
Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников банка.

### Как установить
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`) для установки зависимостей:
```
pip install -r requirements.txt
```
Параметры подлючения к БД находятся в файле `.env`. Переименуйте и заполните `.env.example`.

### Как запустить
```
python manage.py runserver 0.0.0.0:8000
```
Открыть в браузере http://0.0.0.0:8000/

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).