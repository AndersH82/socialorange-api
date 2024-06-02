# API

## Getting Started

To get started with this project, follow the steps below:

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Django

### Setup

1. **Clone the repository:**
   
   git clone [repository-url](https://github.com/AndersH82/socialorange-api.git)

   cd [repository-directory](https://github.com/AndersH82/socialorange-api)
2. Install dependencies:
    pip install -r requirements.txt

3. Apply migrations:
    python manage.py migrate
4. Run the development server:
    python manage.py runserver
5. Access the application:
    Open your web browser and go to http://127.0.0.1:8000/.


### Project Structure
The project is organized into multiple directories, each representing a distinct part of the system:

- ### api: Contains the main Django application files.
- asgi.py
- settings.py
- urls.py
- views.py
- comments: Manages the commenting functionality.
- admin.py
- apps.py
- models.py
- serializers.py
- tests.py
- urls.py
- views.py
- followers: Manages the following functionality.
- admin.py
- apps.py
- models.py
- serializers.py
- tests.py
- urls.py
- views.py
- ### likes: Manages the liking functionality.
- admin.py
- apps.py
- models.py
- serializers.py
- tests.py
- urls.py
- views.py
- ### posts: Manages the posting functionality.
- admin.py
- apps.py
- models.py
- serializers.py
- tests.py
- urls.py
- views.py
- ### profiles: Manages user profiles.
- admin.py
- apps.py
- models.py
- serializers.py
- tests.py
- urls.py
- views.py
- migrations/0002_alter_profile_image.py
- ### migrations: Contains migration files for managing database schema changes.


### Running Frontend Applications
To run a frontend application (HTML, CSS, JavaScript), use the following command in the terminal:
python3 -m http.server
Or use the alias:
http_server

### Running Backend Python Files
To run a backend Python file, use the following command:
python3 app.py


### Deployment

# Social Media API

This project is an API built using Django, which provides functionalities for commenting, liking, posting, and managing user profiles. It's designed to serve as a backend for a social media platform.

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

6. Access the application by opening your web browser and going to `http://127.0.0.1:8000/`.



## Deployment

To deploy this application to Heroku, follow these steps:

1. **Login to Heroku:**
    ```sh
    heroku login
    ```

2. **Create a new Heroku app:**
    ```sh
    heroku create <your-app-name>
    ```

3. **Set environment variables:**
    ```sh
    heroku config:set SECRET_KEY=<your-secret-key>
    heroku config:set DEBUG=False
    ```

4. **Add Heroku Postgres:**
    ```sh
    heroku addons:create heroku-postgresql:hobby-dev
    ```

5. **Deploy the application:**
    ```sh
    git push heroku main
    ```

6. **Run migrations on Heroku:**
    ```sh
    heroku run python manage.py migrate
    ```

7. **Open the application:**
    ```sh
    heroku open
    ```

## Tests


### Manual Tests

POST Test

```
POST /posts/
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
COMMENTS Test
```
POST /comments/
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```

LOG IN Test
```
GET /
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "message": "Welcome to my API for SocialOrange webpage!"
}
```

