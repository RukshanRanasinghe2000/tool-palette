# Tool Palette Backend

This repository contains the backend service for the Tool Palette application. It is a Python-based API built with FastAPI that provides various utility functions, starting with image conversion.

## Folder Architecture

The project is structured to be simple and easy to deploy, particularly with Choreo.

```
.
├── .choreo/
│   └── component.yaml  # Choreo configuration for deployment.
├── .gitignore
├── Dockerfile          # Instructions for building the production Docker image.
├── main.py             # The main FastAPI application file with all API logic.
├── openapi.yaml        # The OpenAPI specification that describes the API endpoints.
└── requirements.txt    # A list of all Python dependencies for the project.
```

-   **`main.py`**: The core of the application, defining all API endpoints and their logic.
-   **`openapi.yaml`**: Provides a static, detailed "menu" of the API, which Choreo uses to build its test console.
-   **`Dockerfile`**: Contains all the commands needed to assemble a runnable Docker image for the application.
-   **`.choreo/component.yaml`**: The deployment descriptor for Choreo, telling it how to build and expose this service.
-   **`requirements.txt`**: Lists the Python packages required by the project.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or later
- `pip` (Python package installer)
- [Docker](https://www.docker.com/get-started) (Optional, for containerized setup)

## Local Development Setup

To run the application on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd tool-palette-backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    The application will be served by Uvicorn. The `Dockerfile` is configured to run on port `8080`.
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8080
    ```
    The API will now be available at `http://localhost:8080`.

## Running with Docker

You can also build and run the application as a Docker container.

1.  **Build the Docker image:**
    ```bash
    docker build -t tool-palette-backend .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8080:8080 tool-palette-backend
    ```
    The API will be accessible at `http://localhost:8080`.

## API Endpoints

The following endpoints are available:

-   **`GET /`**
    -   A welcome endpoint to confirm the service is running.
    -   **Sample Request:**
        ```bash
        curl http://localhost:8080/
        ```
    -   **Sample Response:**
        ```json
        {
            "message": "Welcome to the Tool Palette Backend!"
        }
        ```

-   **`POST /convert-to-webp`**
    -   Converts an uploaded image (e.g., JPG, PNG) or the first page of a PDF file to the WEBP format.
    -   **Request Body:** `multipart/form-data` with a `file` field containing the image.
    -   **Sample Request:**
        ```bash
        # For an image file (e.g., example.png)
        curl -X POST -F "file=@example.png" http://localhost:8080/convert-to-webp -o converted.webp

        # For a PDF file (e.g., example.pdf)
        curl -X POST -F "file=@example.pdf" http://localhost:8080/convert-to-webp -o converted.webp
        ```
    -   **Sample Response:**
        -   The API will return the converted image as binary data with a `Content-Type: image/webp` header. The `curl -o converted.webp` command will save this binary response to a file named `converted.webp`.

## Deployment

This project is pre-configured for deployment on [Choreo](https://wso2.com/choreo/). Simply connect this repository to a new "Service" component in Choreo, and it will use the `Dockerfile` and `.choreo/component.yaml` to build and deploy the application automatically.
