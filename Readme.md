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

Update sudo if needed
    
    sudo apt update

Install Git if haven't
    
    sudo apt install git

Clone Repository
    
    git clone 'https://github.com/DowranRowshenow/SocialMediaWebApp.git'

Go to project directory
    
    cd SocialMediaWebApp

Install `3.13.5` Python version if needed
    
    sudo apt install python3-3.13.5

Install Pip if you haven't
    
    sudo apt install pip

Install Virtual Environment if you haven't 
    
    sudo apt install python3.13.5-venv

Create Virtual Environment
    
    python3 -m venv .venv

Activate Virtual Environment
    
    source venv/bin/activate

Configure mirror repository for pip if needed
    
    mkdir -p ~/.pip
    nano ~/.pip/pip.conf

Write into `pip.conf`
    
    [global]
    index-url=https://mirrors.tencent.com/pypi/simple/
    extra-index-url=https://mirrors.tencent.com/pypi/simple/
    default=https://pypi.org/simple

Install Requirements.txt
    
    python3 -m pip install -r requirements.txt

Install Gettext if you haven't
    
    sudo apt install gettext

Install `MySQL` Server

    sudo apt install mysql-server

Setup `MySQL` Server

    sudo systemctl start mysql
    sudo systemctl enable mysql

Secure `MySQL` Installation
    sudo mysql_secure_installation

Log in to `MySQL`

    sudo mysql -u root -p

Create a Database and User

    CREATE DATABASE myproject CHARACTER SET UTF8MB4;
    CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
    GRANT ALL PRIVILEGES ON myproject.* TO 'myuser'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;

(Optional) Allow Remote Connections 

Edit `/etc/mysql/mysql.conf.d/mysqld.cnf`

Change `bind-address = 127.0.0.1` to `bind-address = 0.0.0.0` to allow remote connections.

Restart `MySQL` Server

    sudo systemctl restart mysql

Install `MySQL CLient` before installing pip `requirements.txt`

    sudo apt install mysql-client libmysqlclient-dev

Test Connection

    mysql -u myuser -p -h localhost myproject
    