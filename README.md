# Todo App

## Getting Started

This project is a simple Todo application using Django, Docker, and PostgreSQL.

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository:
git clone <repository-url>


2. Build and run the Docker containers:

docker-compose up --build

3. Access the application at `http://localhost:8000`.

### Populate database and create superuser

Find web container

    docker ps
    docker exec -it <container_name_or_id> python manage.py makemigrations
    docker exec -it <container_name_or_id> python manage.py migrate
    docker exec -it <container_name_or_id> python manage.py createsuperuser

#### Create users

Access the admin at `http://localhost:8000/admin`
Go to the "Users" section and click "Add User". Fill in the required fields and permissions as needed, then save the new user

### Login Credentials

Use the following credentials to login:
- Username: admin
- Password: admin