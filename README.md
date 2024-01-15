# api_fastapi_python

An API using Python and FastAPI

## Installation

1. **Clone the repository:** Use the following command to clone the repository from GitHub:

    `git clone <repository_url>`

2. **Virtual Environment:** Create a virtual environment in the cloned directory:

-   On Windows:

    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

-   On macOS and Linux:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:** Install dependencies from the `requirements.txt` file using the command:

    `pip install -r requirements.txt`

4. **Configure Environment Variables:** Copy the `.env.example` file to create `.env` and configure appropriate values for environment variables, such as database connection information.

5. **Project Execution:** Use the command to run the project (example with FastAPI and Uvicorn):

    `uvicorn app:app --host $HOST --port $PORT`

6. **Access the Application:** Access the URL specified in Uvicorn (by default, http://localhost:8000) to interact with the application.

**Note:** Make sure you have Python and Git configured on your system before starting the installation process.

## License (TO DO)

# TO DO

-   [ ] Add venv setup guide for read me
-   [ ] Update packages
-   [ ] create script for better dev experiences
