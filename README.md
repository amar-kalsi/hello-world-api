# FastAPI Hello World App

This is a simple FastAPI application that exposes a REST API endpoint `/hello`, printing "Hello world" plus a `SERVICE_VERSION` environment variable.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)

## Getting Started

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Change into the project directory:

    ```bash
    cd hello-world-api
    ```

### Running with Docker

3. Build the Docker image:

    ```bash
    docker build -t hello-world-api .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 8000:8000 -e SERVICE_VERSION=1.0 hello-world-api
    ```

### Running without Docker

3. Install dependencies with [Poetry](https://python-poetry.org/):

    ```bash
    poetry shell
    poetry install
    ```

4. Run the FastAPI application:

    ```bash
    cd app
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

## API Endpoint

- **Endpoint:** `/hello`
- **Method:** GET
- **Response:**
  - Body: `{"content": "Hello world <SERVICE_VERSION>"}`

## Testing

To run tests, use the following command:

```bash
poetry run pytest