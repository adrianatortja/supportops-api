# SupportOps API

A Django REST Framework API for support ticket automation.

SupportOps API allows users to create and manage support tickets while automatically detecting ticket categories, assigning priority levels, generating suggested replies, and providing ticket analytics.

---

## Features

- User registration
- JWT login
- JWT token refresh
- Protected ticket endpoints
- Ticket CRUD
- User-based ownership validation
- Automatic ticket categorization
- Automatic priority detection
- Suggested reply endpoint
- Ticket analytics endpoint
- Filtering, search, and ordering
- Automated API tests
- Swagger/OpenAPI documentation
- Django admin

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- django-filter
- drf-spectacular
- SQLite
- Postman
- Git/GitHub

---

## Main Endpoints

### Auth

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Get JWT access and refresh tokens |
| POST | `/api/auth/refresh/` | Refresh access token |

### Tickets

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tickets/` | List authenticated user's tickets |
| POST | `/api/tickets/` | Create a ticket |
| GET | `/api/tickets/<id>/` | Retrieve a ticket |
| PATCH | `/api/tickets/<id>/` | Update a ticket |
| DELETE | `/api/tickets/<id>/` | Delete a ticket |
| GET | `/api/tickets/<id>/suggested-reply/` | Generate a suggested reply |
| GET | `/api/tickets/analytics/` | View ticket analytics |

### Documentation

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/docs/` | Swagger API documentation |
| GET | `/api/schema/` | OpenAPI schema |

---

## Ticket Filtering, Search, and Ordering

The ticket list endpoint supports filtering, search, and ordering.

Endpoint:

```http
GET /api/tickets/
```

### Filtering

Filter tickets by status:

```http
GET /api/tickets/?status=open
```

Filter tickets by category:

```http
GET /api/tickets/?category=shipping
```

Filter tickets by priority:

```http
GET /api/tickets/?priority=high
```

### Search

Search tickets by subject or message:

```http
GET /api/tickets/?search=refund
```

```http
GET /api/tickets/?search=order
```

### Ordering

Order tickets by creation date:

```http
GET /api/tickets/?ordering=-created_at
```

Order tickets by priority:

```http
GET /api/tickets/?ordering=priority
```

Order tickets by status:

```http
GET /api/tickets/?ordering=status
```

---

## Example Ticket Response

```json
{
  "id": 6,
  "user": 1,
  "subject": "Urgent damaged order",
  "message": "The customer is angry because the order arrived damaged and wants a refund urgently.",
  "status": "open",
  "priority": "high",
  "category": "refund",
  "created_at": "2026-04-30T10:14:57.195743Z"
}
```

---

## Example Suggested Reply Response

```json
{
  "ticket_id": 6,
  "category": "refund",
  "priority": "high",
  "suggested_reply": "We are sorry to hear about the issue with your order. We will review the details and help you with the refund process."
}
```

---

## Example Analytics Response

```json
{
  "total_tickets": 5,
  "open_tickets": 5,
  "pending_tickets": 0,
  "closed_tickets": 0,
  "high_priority_tickets": 4,
  "medium_priority_tickets": 0,
  "low_priority_tickets": 1,
  "refund_tickets": 5,
  "shipping_tickets": 0,
  "technical_tickets": 0,
  "general_tickets": 0
}
```

---

## Automated Tests

This project includes automated API tests for the ticket endpoints.

Current test coverage includes:

- Creating a ticket
- Listing only the authenticated user's tickets
- Retrieving ticket details
- Returning `404 Not Found` for invalid suggested reply requests
- Returning correct analytics counts

Run tests with:

```bash
python manage.py test
```

Or run only ticket tests with:

```bash
python manage.py test tickets
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/adrianatortja/supportops-api.git
cd supportops-api
```

### 2. Create and activate a virtual environment

For Windows PowerShell:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

Swagger documentation will be available at:

```text
http://127.0.0.1:8000/api/docs/
```

---

## Authentication

This API uses JWT authentication.

After logging in, copy the access token and send it in protected requests using:

```text
Authorization: Bearer your_access_token
```

---

## Project Structure

```text
supportops-api/
├── config/
├── tickets/
├── users/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Business Logic

When a ticket is created, the API automatically analyzes the ticket message.

Example message:

```text
The customer is angry because the order arrived damaged and wants a refund urgently.
```

The system detects:

```json
{
  "category": "refund",
  "priority": "high"
}
```

The suggested reply endpoint then generates a support response based on the ticket category.

---

## Project Purpose

This project was built to practice backend API development with Django REST Framework while modeling a real-world customer support workflow.

It demonstrates:

- API design
- Authentication
- Protected endpoints
- User-based data ownership
- CRUD operations
- Filtering, search, and ordering
- Business logic
- Analytics
- Automated testing
- API documentation
- Git/GitHub workflow

---

## Future Improvements

- Add GitHub Actions CI
- Add PostgreSQL
- Add Celery and Redis for background tasks
- Add frontend with React
- Add Docker support