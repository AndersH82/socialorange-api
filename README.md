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
To deploy this application to Heroku, follow these steps:

1. Login to Heroku:
    heroku login
2. Create a new Heroku app:
    heroku create [Heroku App](https://socialorangeapi-e92b8d7040bd.herokuapp.com/)
3. Deploy the application:
    git push heroku main
4. Run migrations on Heroku:
    heroku run python manage.py migrate
5. Open the application:
    heroku open

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
### Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License.

Feel free to customize this `README.md` file further based on your specific project details and requirements.
