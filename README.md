# Event Booking API!

Event Booking API is a RESTful web application built with FastAPI that allows users to create events and book seats for them.  
The system supports secure authentication, event management, and real-time seat booking with business logic validation.

Users can:
- register and login,
- create and manage events,
- book available seats,
- view their own events and bookings.

The application uses PostgreSQL as the database and Alembic for schema migrations.  
JWT is implemented for secure access to protected endpoints.

---

# Features

- User Authentication: Secure registration and login using JWT tokens.
- Event Management: Create and list events with capacity control.
- Seat Booking: Book seats with live validation of availability.
- Business Logic Validation:
  - One user cannot book the same event twice.
  - Seats cannot exceed the event capacity.
  - Users can only see their own events and bookings.
- PostgreSQL Database: Reliable relational database with Alembic migrations.
- JWT Protected Routes: All private routes require authentication.
- Swagger UI: Interactive API documentation and testing.

---

## Technologies Used

- **FastAPI** for building REST API.
- **PostgreSQL** as relational database.
- **SQLAlchemy 2.0** for ORM.
- **Alembic** for database migrations.
- **JWT (OAuth2 Password Flow)** for authentication.
- **Docker & Docker Compose** to run PostgreSQL.
- **Passlib (bcrypt_sha256)** for password hashing.
- **Pydantic v2** for data validation and schemas.

---

## Requirements

Before running the project, make sure you have:

- Python 3.10+
- Docker & Docker Compose
- PostgreSQL client (optional, for debugging)
- pip or virtualenv

---

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/Dmytro-Burdeniuk/fastapi_rest_booking.git>
cd fastapi_rest_booking
```

### 2. Create venv

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies 

```bash
pip install -r requirements.txt
```

### 4. Create .env file

```bash
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=

DATABASE_URL=
SECRET_KEY=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

### 5. Run Postgres using Docker

```bash
docker compose up -d
```

### 6. Run migratioms using Alembic

```bash
alembic upgrade head
```

### 7. Use!!!

```bash
uvicorn src.main:app --reload
```