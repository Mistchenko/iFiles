# iFiles
(Flask) Upload files


Локальный сервер для загрузки фалов (фотки, видео, и прочее...) из iPhone


## Настройка pyCharm, 


Для своих настроек добавить в поле:
"Additional options" --host=0.0.0.0 --port=5000

Для autoreload: 
FLASK_ENV = development
FLASK_DEBUG = 1


## Docker

Собрать: `docker-compose build`

Запустить: `docker-compose up`

Оболочка: `docker-compose run --rm flask bash`



