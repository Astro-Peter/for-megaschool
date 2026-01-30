# FastAPI Project

This project presents a simple FastAPI application with endpoints for serving requests.

## Endpoints
- `GET /`: Returns a simple greeting.

## Docker
To run the application using Docker:

```bash
# Build the Docker image
docker build -t myfastapiapp .

# Run the Docker container
docker run -d --name myfastapiapp -p 80:80 myfastapiapp
```

## Running Tests
To run the tests:

```bash
pytest
```