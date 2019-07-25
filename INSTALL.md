## 1. Добавить в файл .env
```
NOTEBOOK_PASSWORD=password
POSTGRES_PASSWORD=password
POSTGRES_TWIN_PASSWORD=password
```

## 2. Собрать
создать том `docker volume create postgres-twin-data`

сборка образов `docker-compose build`

запуск контейнеров `docker-compose up -d`


## 3. Инициализация postgres
```
twin_queue - папка репозитория
docker exec -it twin_queue_postgres_1 sh
psql -U postgres -d postgres -a -f /opt/app/docs/init.sql
```

### 3.1 Задание пароля пользователя
```
psql -U postgres -d postgres
alter user twin with password 'password';
```

### 4. Инициализация django
```
docker exec -it twin_queue_app_1 python manage.py migrate
docker exec -it twin_queue_app_1 python manage.py collectstatic
```

## 5. Проверить можно используя API по адресу
http://localhost:8050/create/ - создание

http://localhost:8050/ - список всех

http://localhost:8050/1/ - задача с номером 1


## 6. notebook - http://localhost:8055

пароль password (см. п.1)
