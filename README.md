# First django project

## Install

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/mari-sanina/django-3.0.git
   cd django-3.0
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python3 -m venv env
   source env/bin/activate  # Для Windows: env\Scripts\activate

3. Установите зависимости:
   ```bash
    pip install -r requirements.txt
   
4. Выполните миграции:
   ```bash
   python manage.py migrate

5. Создайте файл .env и настройте переменные окружения (на основе .env.example).


## Run
1. Для разработки:
   ```bash
   python manage.py runserver