# To-Do Application (FastAPI + Beanie + MongoDB)

A simple To-Do REST API built with FastAPI, Beanie (MongoDB ODM), and JWT-based authentication.

## Features
- User registration and CRUD for users
- Todo CRUD
- JWT authentication (login issues a Bearer token)
- OpenAPI / Swagger UI

## Requirements
- Python 3.13
- MongoDB instance
- See dependencies in [requirements.txt](backend/app/requirements.txt)

## Quick setup
1. Create and activate a virtual environment (recommended).
2. Install dependencies:
   ```sh
   pip install -r backend/app/requirements.txt
   ```
3. Configure environment variables (example in `.env`):
   - JWT_SECRET_KEY
   - JWT_REFRESH_KEY
   - DATABASE_URL
   - DATABASE_NAME

4. Initialize DB on startup — the app calls [`init_db`](backend/app/core/database.py) at startup.

## Run
From the project root (parent of the `app` package) run:
```sh
Fastapi dev app.py
```
See app entry: [`backend/app/app.py`](backend/app/app.py) and DB init: [`backend/app/core/database.py`](backend/app/core/database.py).

## API overview

Base path: `/api` (see router inclusion in [`backend/app/routes/router.py`](backend/app/routes/router.py))

Auth:
- POST `/api/auth/login` — exchange email + password for a JWT access token. (Implemented in [`backend/app/routes/auth.py`](backend/app/routes/auth.py), function [`login_for_access_token`](backend/app/routes/auth.py))

Users:
- POST `/api/users/` — create a user (request body uses `email` + `password`) — see schemas in [`backend/app/schemas/user.py`](backend/app/schemas/user.py) and logic in [`backend/app/services/user.py`](backend/app/services/user.py)
- GET `/api/users/` — list users (protected)
- GET `/api/users/{user_id}` — get a user by id (protected)
- PUT `/api/users/{user_id}` — update user (protected)
- DELETE `/api/users/{user_id}` — delete user (protected)

Todos:
- POST `/api/todos/` — create todo
- GET `/api/todos/` — list todos
- GET `/api/todos/{todo_id}` — get todo
- PUT `/api/todos/{todo_id}` — update todo
- DELETE `/api/todos/{todo_id}` — delete todo

Relevant files:
- Auth dependency & JWT helpers: [`backend/app/dependencies/auth.py`](backend/app/dependencies/auth.py) (see [`get_current_user`](backend/app/dependencies/auth.py) and `oauth2_scheme`)
- User model: [`backend/app/models/user.py`](backend/app/models/user.py)
- User routes: [`backend/app/routes/user.py`](backend/app/routes/user.py)
- User services: [`backend/app/services/user.py`](backend/app/services/user.py)
- Auth routes: [`backend/app/routes/auth.py`](backend/app/routes/auth.py)

## Authentication (how to use)
- Obtain token:
  - Use Swagger UI (open `/docs`) or curl:
    ```sh
    curl -X POST "http://localhost:8000/api/auth/login" \
      -d "username=youremail@example.com&password=yourpassword"
    ```
  - The login route expects the email in the OAuth2 form field `username` (see [`login_for_access_token`](backend/app/routes/auth.py)).

- Use token to call protected endpoints:
  - In Swagger UI click "Authorize" and paste: `Bearer <ACCESS_TOKEN>`
  - Or curl:
    ```sh
    curl -H "Authorization: Bearer <ACCESS_TOKEN>" \
      http://localhost:8000/api/users/
    ```

