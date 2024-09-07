## Django-приложение, магазин с реализацией древовидного меню.

### Стек технологий:

 - ![alt text](https://img.shields.io/badge/Python-3.11.5-grey?style=plastic&logo=python&logoColor=white&labelColor=%233776AB)

 - ![alt text](https://img.shields.io/badge/Django-5.1.1-grey?style=plastic&logo=django&logoColor=white&labelColor=%23092E20)

 - ![alt text](https://img.shields.io/badge/PostgreSQL-15.3-grey?style=plastic&logo=postgresql&logoColor=white&labelColor=%234169E1)

 - ![alt text](https://img.shields.io/badge/Docker-v4.25.0-grey?style=plastic&logo=docker&logoColor=white&labelColor=2496ED)

### Описание проекта
Разработано Django-приложение, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

***

### Запуск через Docker
<details>
<summary>Для запуска через Docker необходимо:</summary>

- Клонировать проект на собственный диск в новом каталоге
-  <details>
   <summary>Прописать переменные окружения в файле `.env.sample`</summary>
   
    ```dotenv
    SECRET_KEY='Секретный ключ Django'
    DEBUG='True/False', например: True
    
    # PostgreSQL
    POSTGRES_DB_NAME='Название базы данных', например: 'name_of_db' или 'django_shop_tree_menu'
    POSTGRES_DB_USER='Пользователь базы данных', например: 'db_user' или 'postgres'
    POSTGRES_DB_PASSWORD='Пароль пользователя базы данных', например: 'your_password'
    POSTGRES_DB_HOST='Хост базы данных', например: '127.0.0.1' или 'localhost' или 'db' для Docker
    POSTGRES_DB_PORT='Порт базы данных', например: '5432'
    
    # Superuser
    ADMIN_USERNAME=admin
    ADMIN_EMAIL=admin@example.com
    ADMIN_PASSWORD=admin
    ```
   </details>

- Ввести в терминале команду:
    ```python
    docker-compose up --build
    ```
    > Происходит сборка образа контейнера согласно инструкции в файле Dockerfile и последовательный запуск всех контейнеров согласно инструкции в файле docker-compose.yaml

</details>

***

### Для завершения работы необходимо:

 - Нажать комбинацию клавиш `CTRL + C` в окне терминала

***

<b>Connect with me:</b>
<p align="left">
   <a href="mailto:platonovpochta@gmail.com"><img src="https://img.shields.io/badge/gmail-%23EA4335.svg?style=plastic&logo=gmail&logoColor=white" alt="Gmail"/></a>
   <a href="https://wa.me/79217853835"><img src="https://img.shields.io/badge/whatsapp-%2325D366.svg?style=plastic&logo=whatsapp&logoColor=white" alt="Whatsapp"/></a>
   <a href="https://t.me/platonov_sm"><img src="https://img.shields.io/badge/telegram-blue?style=plastic&logo=telegram&logoColor=white" alt="Telegram"/></a>
</p>
