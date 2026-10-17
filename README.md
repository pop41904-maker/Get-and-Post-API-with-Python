# FastAPI User Registration API

A simple and secure user registration API built with **FastAPI**, **Pydantic** for data validation, and **SQLite** (via a custom database module) for storage. It features password hashing using **SHA-512** with a unique **cryptographic salt** for each user.

## Features

- **Data Validation**: Strict validation for usernames, passwords, and email formats using Pydantic.
- **Secure Password Hashing**: Passwords are securely hashed using `hashlib.sha512` and a unique `uuid4` generated salt.
- **Automatic Documentation**: Interactive API documentation provided automatically by FastAPI (Swagger UI / ReDoc).

## API Endpoints

### Create User
* **URL**: `/user`
* **Method**: `POST`
* **Tags**: `Create User`
* **Request Body**:
  ```json
  {
    "Name": "JohnDoe",
    "Password": "securepassword123",
    "Email": "johndoe@example.com"
  }
  ```
* **Validation Rules**:
  - `Name`: String (2 to 18 characters)
  - `Password`: String (Minimum 6 characters)
  - `Email`: Valid email string format
* **Success Response**:
  ```json
  {
    "massage": true,
    "User status was create": true
  }
  ```

## Project Structure

```text
├── data/
│   └── data.py       # Database connection utilities (connect_DB, cursor_connect)
├── main.py           # Main application file containing endpoints and schemas
└── README.md         # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn (for running the server)
- Pydantic (with `email-validator`)

### Installation

1. Clone the repository and navigate to the project folder.
2. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn pydantic[email-validator]
   ```

### Running the Application

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### API Documentation

Once the server is running, you can explore and test the API directly through the automatically generated interactive docs:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
