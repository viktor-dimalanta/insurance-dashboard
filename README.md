# Insurance Dashboard with FastAPI Backend and Nuxt 3 Frontend

This project consists of a backend built with FastAPI and SQLAlchemy connected to a PostgreSQL database, and a frontend built with Nuxt 3. The backend provides API endpoints for managing clients and quotes, while the frontend allows users to interact with the backend.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Setup](#backend-setup)
  - [Requirements](#requirements)
  - [Docker Setup](#docker-setup)
- [Running the Project](#running-project)
- [Testing](#testing)
- [License](#license)

---

## Project Overview

This project consists of two main parts:

- **Backend**: FastAPI application using SQLAlchemy to interact with a PostgreSQL database. It provides endpoints for managing clients and quotes.
- **Frontend**: Nuxt 3 application that interacts with the backend to list, create, and manage clients and quotes.

---

## Project Dashboard (Kanban)

- Project Dashboard (https://github.com/users/viktor-dimalanta/projects/2/views/1)
  
---

## Project Setup

The backend is implemented with FastAPI, SQLAlchemy, and PostgreSQL. It exposes REST API endpoints to interact with client data and quote records.

### Requirements

- **Python 3.9+**
- **PostgreSQL 13+**
- **Docker** (to run the app with all services)

### Docker Setup

The backend is containerized with Docker. You'll need to install Docker on your local machine.

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd backend

2. Make sure your `docker-compose.yml` file is set up correctly in the backend directory.

    ```yaml
      version: '3.8'
      
      services:
        backend:
          build:
            context: ./backend
          volumes:
            - ./backend:/app
          ports:
            - "8000:8000"
          depends_on:
            - db
          environment:
            - DATABASE_URL=postgresql+asyncpg://postgres:Abc12345@db:5432/insurance_db
            - SECRET_KEY=QYJurIw6szO4pCKHUNfGzaozL2AAOj/WHecuiZi+dOU=
      
        frontend:
          build:
            context: ./frontend
          volumes:
            - ./frontend:/app
          ports:
            - "3000:3000"
      
        db:
          image: postgres:13
          environment:
            POSTGRES_DB: insurance_db
            POSTGRES_USER: postgres
            POSTGRES_PASSWORD: Abc12345
          volumes:
            - db_data:/var/lib/postgresql/data
          ports:
            - "5432:5432"
      
      volumes:
        db_data:

###  Running the Project

   In the root directory (where the docker-compose.yml is located), run the following command to start the backend and frontend services:
   
    ```
    docker-compose up --build
    ```

  This command will build the Docker containers for both the backend and frontend services. Once the containers are up and running, you should be able to access:

    * Backend (FastAPI): http://localhost:8000
    * Frontend (Nuxt 3): http://localhost:3000

---

### Postman Endpoints

Here are the API endpoints you can use with Postman to interact with the FastAPI backend.

1. Create a Client
   
   URL: POST /clients

   ```
    {
      "name": "John Doe",
      "email": "john@example.com"
    }
   ```

3. List All Clients
   
   URL: GET /clients

   ```
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
      }
    ]
   ```
   
4. Create a Quote
   
   URL: POST /quotes

   ```
    {
      "amount": 500,
      "client_id": 1
    }
   ```

5. List All Quotes for a Client
   
   URL: GET /clients/{client_id}/quotes
   
   Example: GET /clients/1/quotes

   ```
    [
      {
        "id": 1,
        "amount": 500,
        "client_id": 1,
        "quote_text": "Sample quote text"
      }
    ]
   ```
   
6.  Get a Specific Quote
   
    URL: GET /quotes/{quote_id}
    
    Example: GET /quotes/1

   ```
    {
      "id": 1,
      "amount": 500,
      "client_id": 1,
      "quote_text": "Sample quote text"
    }
   ```

----

# Areas for Improvement

### Backend
✅ Add Authentication: Currently, login is mocked. Implement JWT-based auth.

✅ Add Pagination: For large datasets, paginate clients and quotes.

✅ Unit Tests: Add automated tests using pytest for endpoints and models.

✅ Validation: Add stricter validation for email, amount, etc.

✅ Error Handling: Implement custom exception handlers for better error responses.

✅ Environment Configs: Use .env files and pydantic.BaseSettings for clean configuration.

### Frontend
✅ Form Validation: Add proper validation using VeeValidate or Zod.

✅ Notification System: Show toasts for success/failure actions.

✅ Improved UI: Use a component library like Vuetify or Tailwind UI.

✅ Authentication Flow: Replace mocked token with real login/logout + protected routes.

### DevOps
✅ Production Docker Setup: Add Dockerfile for production (multi-stage build).

✅ CI/CD Pipeline: Add GitHub Actions or GitLab CI for auto testing and deployment.

✅ Database Migrations: Introduce Alembic or use SQL-based version control.

---

### License

Developed by

Viktor Angelo Dimalanta, MSIT https://www.linkedin.com/in/viktor-dimalanta-msit/
