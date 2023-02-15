## Prerequisites

- Database configuration (check additional configuration options below)

### Server installation Instructions

- **clone the project**
  ```bash
   $ git clone git@github.com:shahid-ullah/peshajibi.git
  ```
- **change to project directory**
  ```bash
  $ cd peshajibi
  ```
- **create virtual environment and active virtual environment**
  ```bash
    $ virtualenv venv
    $ source venv/bin/activate
  ```
- **Install project dependencies**
  ```bash
    $ pip install -r requirements/requirements.txt.production
  ```
- **Run migration**
  ```bash
    $ python manage.py migrate
  ```
- **collect static files**
  ```bash
    $ python manage.py collectstatic
  ```
- **Start development server**
  ```bash
    $ python manage.py runserver
  ```

### Additional Instructions

- create .env file in project root directory and put required value

```py
  SECRET_KEY=''
  DEBUG=False
  DEFAULT_DATABASE=''
  MYSQL_DB_NAME=''
  MYSQL_DB_USER=''
  MYSQL_DB_PASSWORD=''
  MYSQL_DB_HOST=''
  MYSQL_DB_PORT=''
```
