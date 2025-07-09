# INSTALLATION

Create `.env` and enter your keys

    SECRET_KEY=
    EMAIL_HOST=
    EMAIL_PASSWORD=
    MYSQL_DATABASE=
    MYSQL_USER=
    MYSQL_PASSWORD=
    MYSQL_HOST=

Get a new `Secret key` from django and copy to the `.env`

    py manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())


# `WINDOWS`

Install and Setup `Python` if you dont have. Project uses `3.13.5` version
- https://www.python.org/downloads/

Install and Setup `Git` if you dont have. 
- https://git-scm.com/downloads

Install and Setup `MySql` if you dont have
- https://www.mysql.com/downloads/

Clone `Git` repository

    git clone https://github.com/DowranRowshenow/SocialMediaApp/SocialMediaApp.git

Create virtual environment and activate

    py -m venv .venv
    .venv/Scripts/Activate

Open `MySql` terminal and create new database and user

    CREATE DATABASE your_db_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_db_password';
    GRANT ALL PRIVILEGES ON your_db_name.* TO 'your_db_user'@'localhost';
    FLUSH PRIVILEGES;

Finally run project

    py manage.py makemigrations accounts
    py manage.py makemigrations rooms
    py manage.py makemigrations friends
    py manage.py makemigrations notifications
    py manage.py makemigrations main
    py manage.py makemigrations

    py manage.py migrate
    py manage.py collectstatic
    py manage.py compilemessages
    py manage.py runserver

Additionally create super user after `migrate`

    py manage.py createsuperuser


# `LINUX`

