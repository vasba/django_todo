# Todo App

## Getting Started

This project is a simple Todo application using Django, Docker and containerized PostgreSQL.

### Prerequisites

- python3
- Docker
- Docker Compose

### Running the Application

1. Clone the repository:

```
git clone <repository-url>
```

2. Change default credentials for PostgreSQL

Credentials in [docker-compose.yml](docker-compose.yml) and [settings.py](todo_app/todo_app/settings.py) under DATABASES should be changed and should match.

2. Build and run the Docker containers:

```
    docker-compose up --build -d
```

3. Populate database and create superuser

Find web container

```
    docker ps
```

Then perform the commands below.

```
    docker exec -it <container_name_or_id> python manage.py makemigrations
    docker exec -it <container_name_or_id> python manage.py migrate
    docker exec -it <container_name_or_id> python manage.py createsuperuser
```

WARNING!!!

PostgresSql saves data under docker volume postgres-data, If you remove it the above commands needs to be redone.

4. Create users

Access the admin at `http://localhost:8000/admin`
Go to the "Users" section and click "Add User". Fill in the required fields and permissions as needed, then save the new user

5. Access the application at `http://localhost:8000`.

6. Log in as one of the created users

7. Start creating TODOs

## Testing

Clone the repository

```
    git clone <repository-url>
```

Switch to folder where code have been cloned, default above is django_todo

```
    cd django_todo/todo_app
```

Install requirements

```
    pip install -r requirements.txt
```

Run Tests

```
    python3 manage.py test todos.tests
```