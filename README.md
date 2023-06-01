# Todo App Api

This Todo App API is built using Django Rest Framework. It provides endpoints for managing tasks and tags, as well as user authentication using Basic Authentication.

## Features
- CREATE a todo item
- READ one todo item
- READ all todo items
- UPDATE a todo item
- DELETE a todo item
- User Registration: Users can register and create an account.
- User Login: Registered users can log in to their accounts.


## Technologies Used

- Backend:
  - 1. Python 3.8+
  - 2. Django 3.1+: Python-based web framework for building robust web applications.
  - 3. Django Rest Framework (DRF) 3.1+: Toolkit for building RESTful APIs.
  - Basic Authentication : Library for implementing Basic authentication in Django.
 
- Testing:
1. Postman Collection


## Installation and Setup

1. Set up Project:
- Create and activate a virtual environment.
```bash
mkvirtualenv env
```
- activate virtualenv in windows
```
env/Scripts/activate
```
- activate virtualenv in linux/macOs
```
source env/bin/activate
```
2. Clone the repository:
```bash
git clone https://github.com/as4c/Todo-Api.git
```
3. Change into the project directory:
```bash
cd Todo-Api
````
- Install the required Python dependencies from the `requirements.txt` file:
  ```
  pip install -r requirements.txt
  ```
- Set up the database and apply migrations:
  ```
  python manage.py migrate
  ```
- Start the Django development server:
  ```
  python manage.py runserver
  ```


4. Open your web browser and visit `http://127.0.0.1:8000` to access the application.

## Configuration

Before running the app, make sure to configure the following settings:

- Backend:
- Update the database settings in the `settings.py` file.




## Authentication

- The API endpoints related to tasks and tags require authentication using Basic Authentication.
- To access the authenticated endpoints, include the username and password in the `Authorization` header of the HTTP request using Basic Authentication.
- To signup, send a POST request to the `/users/signup/` endpoint with the required user details.
- To login, send a POST request to the `/users/login/` endpoint with the username and password included in the `Authorization` header.
- To logout, send a GET request to the `/users/logout/` endpoint.

## Endpoints

- **Create Todo**: Create a new todo task.

  - URL: `/api/create-todo/`
  - Method: POST

- **Todo List**: Retrieve a list of all todo tasks.

  - URL: `/api/todos/`
  - Method: GET

- **Todos**: Retrieve, update, or delete a specific todo task.

  - URL: `/api/todo/<int:pk>/`
  - Method: GET, PUT, DELETE

- **Create Tag**: Create a new tag.

  - URL: `/api/create-tag/`
  - Method: POST

- **Tags**: Retrieve a list of all tags.

  - URL: `/api/tags/`
  - Method: GET

- **Detail Tags**: Retrieve, update, or delete a specific tag.

  - URL: `/api/tags/<int:pk>/`
  - Method: GET, PUT, DELETE

- **Signup**: User signup to create an account.

  - URL: `/users/signup/`
  - Method: POST

- **Login**: User login to authenticate using Basic Authentication.

  - URL: `/users/login/`
  - Method: POST

- **Logout**: User logout to end the Basic Authentication session.

  - URL: `/users/logout/`
  - Method: GET


## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/fix:
```
git checkout -b feature/my-feature
```
markdown

3. Make your changes and commit them:
```
git commit -m "Add new feature"
```


4. Push the changes to your forked repository:
```bash
git push origin feature/my-feature
```


5. Open a pull request on the original repository.

## License

This project is licensed under the [MIT License](LICENSE).
