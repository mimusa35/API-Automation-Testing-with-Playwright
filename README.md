# API Automation Testing with Playwright

## **Overview**
This project demonstrates automated API testing for the JSONPlaceholder (`https://jsonplaceholder.typicode.com`) public mock API using Playwright. The tests cover CRUD operations (Create, Read, Update, Delete) for the `/todos` endpoint and validate response status codes, body content, response structure, and performance metrics (response time).

## **Environment Setup**
To set up the environment for running the tests, follow these steps:

1. **Install Python**:
   Ensure Python 3.12 or later is installed. Version 3.12.6 is used in this project. You can download it from [python.org](https://www.python.org/downloads/). To check the Python version, use the following command:
   ```bash
     python --version
   ```

2. **Install Dependencies**:
   - Clone this repository to your local machine.
   ```bash
     git clone <repository_url>
     cd <repository_directory>
   ```
   - Create a virtual environment (for Windows) on the project root directory using the following command:
   ```bash
     python -m venv venv
   ```
   - Activate the virtual environment (for Windows) using the following command:
   ```bash
     venv\Scripts\activate
   ```
   
   - Once the virtual environment is activated, you can install the required dependencies using the following command:
   ```bash
     pip install -r requirements.txt
   ```

## **Folder Structure**
```
├── tests/
│   ├── test_get_todos.py        # GET endpoint tests
│   ├── test_post_todos.py       # POST endpoint tests
│   ├── test_put_todos.py        # PUT endpoint tests
│   └── test_delete_todos.py     # DELETE endpoint tests
├── .github/
│   └── workflows/
│       └── api_tests.yml        # CI/CD workflow configuration
├── requirements.txt             # Dependencies
├── README.md                    # Documentation
```
## **Running Tests**

1. **Run a single test**:
   - To execute a single test file, use the following command:
   ```bash
     python -m pytest path_to_test_file.py
   ```
     
   - If you want more detailed output for debugging or to see test results clearly, use the -v (verbose) and -s (show output) options:
   ```bash
     pytest -v -s path_to_test_file.py
   ```
   Example: Running the test file `test_get_todos.py` located in the `tests` folder:
   ```bash
     pytest -v -s tests/test_get_todos.py
   ```

2. **Run all tests**:
   - To run all tests in the project, navigate to the root directory of the project (where pytest is installed) and simply run:
   ```bash
     python -m pytest
   ```
     
## **Test Scenarios Covered**
The following scenarios are covered for the `/todos` endpoint:

**GET Requests**
1. GET /todos:
   - Validate that the API returns a list of to-do items.
   - Verify the response structure includes `userId`, `id`, `title`, and `completed` for each to-do item.
   - Ensure that the response is a valid list and not empty.
   - Validate the response time is under 500ms.
   - Validate the response status is `200 OK`.

2. GET /todos/{id} (Invalid Request):
   - Verify that requesting a non-existent to-do item (e.g., `id=9999`) returns a `404 Not Found` status.

**POST Requests**
1. POST /todos (Valid Request):
   - Validate that a new to-do item is created with the correct data (`title`, `completed`).
   - Verify the response contains the id of the newly created to-do item.
   - Verify the response status is `201 Created`.
   - Validate that the response time is under 500ms.

2. POST /todos (Empty Payload):
   - Test behavior when sending an empty payload.
   - JSONPlaceholder mock API does not strictly validate required fields, so it returns a 201 Created status despite the empty payload. 
   - Validate that the response contains an id, indicating the resource was created.

**PUT Requests**
1. PUT /todos/{id} (Valid Request):
   - Validate that an existing to-do item is updated correctly with the provided data (`title`, `completed`.
   - Verify the response status is `200 OK`.
   - Ensure that the updated data is reflected correctly in the response. 
   - Validate that the response time is under 500ms.

2. PUT /todos/{id} (Invalid Request):
   - Verify that attempting to update a non-existent to-do item (e.g., `id=9999`) returns a `404 Not Found` or a `500 Internal Server Error`, based on mock API behavior.

**DELETE Requests**
1. DELETE /todos/{id} (Valid Request):
   - Validate that an existing to-do item is deleted successfully.
   - Verify the response status is `200 OK`.
   - Ensure that the response body is an empty JSON object ({}), indicating successful deletion.
   - Validate that the response time is under 500ms.

2. DELETE /todos/{id} (Invalid Request):
   - Verify that attempting to delete a non-existent to-do item (e.g., `id=9999`) returns a `404 Not Found` or `200 OK` (based on mock API behavior).
   - Note: JSONPlaceholder mock API may return `200 OK` even for non-existent resources.

## **Assumptions Made**
   - The JSONPlaceholder API mock does not enforce strict validation, which is why some tests (like the empty payload POST) may behave differently than expected in a real-world API.
   - All the tests assume that the API is reachable and responsive at `https://jsonplaceholder.typicode.com`.
   - A response time threshold of `500ms` is used for validating API performance, assuming network latency. Response times may vary depending on internet speed.

## **Additional Resources**
   - [Playwright Documentation](https://playwright.dev/python/docs/api/class-playwright)
   - [GitHub Actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)
