## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:
```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```

Загрузить тестовые данные:
```bash
python manage.py loaddata fixtures.json
```



* Команда для запуска приложения
```bash
python manage.py runserver
```
