# Media Processing Platform Backend

This is the backend service for the AI-powered media processing platform as part of the Storyvord Backend Engineering Intern Assessment.

## Technologies Used
- Django + Django REST Framework
- Celery (Task Queue)
- Redis (Message Broker & Result Backend)
- PostgreSQL (Database)
- Docker & Docker Compose
- JWT (Authentication)

## Features
- **JWT Authentication**: Secure user registration and login.
- **Task Submission API**: Submit mock AI processing tasks (Text Summarization, Sentiment Analysis, Image Captioning).
- **Asynchronous Processing**: Celery workers handle tasks in the background.
- **Task Tracking & Result Retrieval**: Poll task status and retrieve results once completed.
- **Failure Handling**: Automatic retries for transient failures with exponential backoff.

## Prerequisites
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

## Installation & Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <your-repository-url>
   cd Media-Processing-Platform/media_processing_platform
   ```

2. **Run the application using Docker Compose**:
   ```bash
   docker-compose up --build
   ```
   This command will:
   - Build the web and celery containers.
   - Start PostgreSQL and Redis databases.
   - Run database migrations automatically.
   - Start the Django development server on `http://localhost:8000`.

## API Documentation

### 1. Authentication

**Register a User**
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpassword123", "email": "test@example.com"}'
```

**Login (Get JWT Token)**
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpassword123"}'
```
*Note the `access` token returned in the response.*

### 2. Task Processing

**Submit a Task**
Supported `task_type` values: `text_summarization`, `sentiment_analysis`, `image_captioning`.
```bash
curl -X POST http://localhost:8000/api/tasks/ \
     -H "Authorization: Bearer <your-access-token>" \
     -H "Content-Type: application/json" \
     -d '{
           "task_type": "text_summarization",
           "input_data": {"text": "This is a very long text that needs to be summarized by the AI."}
         }'
```
*Response will contain the task `id` and status `pending`.*

**Retrieve Task Status & Result**
Use the `id` from the previous step.
```bash
curl -X GET http://localhost:8000/api/tasks/<task-id>/ \
     -H "Authorization: Bearer <your-access-token>"
```
*Keep polling this endpoint. Once status is `completed`, the `result_data` will contain the mock AI output.*
