# new-words-backend

Перед первым запуском:
```bash
cp .env.example .env
```

Запуск:
```bash
docker-compose up
```

Создание супер пользователя:
```bash
make createsuperuser
```

Зайти в админку джанги
http://localhost:8000/admin/

Добавить текст
http://localhost:8000/text/add/ или  
http://localhost:8000/admin/new_words/text/add/


Распарсить сохраненные тексты на слова
```bash
make process_texts
```
