# EXPLANATION.md

## Architectural Decisions

- **Django & DRF**: Used as the foundational framework due to its robust ecosystem and rapid development capabilities, aligning with the assessment's technology stack.
- **Docker Compose**: Implemented to provide a predictable and reproducible environment. This eliminates the "works on my machine" problem and effortlessly manages the complex interplay between Django, Celery, PostgreSQL, and Redis.
- **Celery with Redis**: Chosen as the task queue and broker combination. Redis is extremely fast and acts as both the message broker and result backend. Celery's robust retry mechanisms and exponential backoff were leveraged for failure handling.
- **UUIDs for Tasks**: Used UUIDs for the `ProcessingTask` primary keys to prevent ID guessing and improve security when accessing task results.

## Tradeoffs

- **Mock AI Processing vs. Real AI Integration**: To keep the project self-contained and avoid requiring third-party API keys (like OpenAI), mock processing with a `time.sleep` delay was used. This successfully demonstrates the asynchronous architecture without adding external dependencies.
- **Development Server in Docker**: The `docker-compose.yml` uses the Django `runserver` for simplicity in this assessment. In a true production environment, Gunicorn with Nginx would be used.

## Challenges & Debugging

- **Handling Celery Dependencies**: Setting up Celery to correctly interface with the Django ORM inside Docker required careful configuration of environment variables (`DATABASE_URL`, `CELERY_BROKER_URL`). I ensured that the `depends_on` block in `docker-compose.yml` was utilized so that Celery and the Web app wait for Redis and PostgreSQL.
- **Failure Simulation**: To demonstrate Celery's failure handling, I injected a random 20% chance of a generic exception occurring in the task processing. Celery's `max_retries` and `countdown` features gracefully handle this by retrying.

## Alternative Approaches Considered

- **Using SQLite & local memory broker**: I initially considered avoiding Docker and using SQLite and a local memory broker for Celery to make it run bare-metal easily. However, Celery strongly advises against local filesystem/memory brokers for anything resembling production or robust queues. Thus, adopting Docker was the best path forward to provide a professional, clean setup.

## AI Usage Disclosure

- AI tools were utilized to scaffold the boilerplate for Django configuration, Celery worker setup, and standard DRF ViewSets.
- The `process_media_task` Celery function logic (including the random failure simulation and mock outputs) was generated and refined to specifically address the assessment's requirements for graceful failure and realistic mock data.
