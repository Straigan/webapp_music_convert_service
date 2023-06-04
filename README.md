# Webapp music convert service

##  Webapp music convert service - это web-приложение на Flask.

При разработке приложения применялись технлогии: Flask, PostgreSql, SQLAalchemy, docker-compose.
Данное web-приложение конвертирует аудиозапись формата wav в формат mp3.    
В данном приложении пользователь проходит регистрацию. Далее используя свой UUID, токен доступа отправляет на сайт
аудиозапись формата wav, в ответ получает ссылку для скачивания данной аудиозаписи в формате mp3.

# Сборка репозитория и запуск

## Настройка

Выполните в консоли:

git clone https://github.com/Straigan/webapp_music_convert_service.git

Необходимо создать файл .env и присвоить значения следующим переменным  

Пример файла .env:  
FLASK_APP='webapp'  
DATABASE_URL='postgresql://flaskuser:flaskpassword@postgres:5432/flaskdb'  
SECRET_KEY='weq1312eqwe'

Данные для формирования подключения к БД в docker, указываются в 'docker/.env-postgresql'.  

Пример файла .env-postgresql:  
DATABASE_PORT=5432  
DATABASE_DIALECT=postgresql  
POSTGRES_DB=flaskdb  
POSTGRES_USER=flaskuser  
POSTGRES_PASSWORD=flaskpassword  

## Запуск web-приложения на ОС Linux:

Находясь в корневой директории проекта, введите в консоли:  
docker-compose up  

Для регистрации получении возмжожности конвертирования записи из wav в mp3,
необходимо сначала зарегистрироваться, для ключа name укажите имя пользователя:  
curl -i -H "Content-Type: application/json" -X POST -d '{"name": "ilya"}' http://localhost:5000/users/registration  
прийдет ответ с уникальным индификационным номером и токеном доступа:
{"access_token":"11e14a6b-b091-4490-b114-82ce78781dd0","id":2}  

Далее загрузка файла на сервер происходит через программу postman,
не обходимо указать токен досутпа, уникальный индификкационный номер и прикрепить файл.
![Загрузка файла wav на сервер](docs/1.jpg)
прийдет ответ ввиде ссылки для скачивания:  
http://localhost:5000/record?id=16&user=2

Далее в программе Postman выбираем GET запрос, адрес сайта для скачивания файла http://localhost:5000/record и 
указываем ключи id и user, полученные с предыдущего шага
![Скачивание файла mp3 c сервера](docs/2.jpg)