import time
from playwright.sync_api import sync_playwright

# Test for POST /todos (Valid request)
def test_post_todo():
    with sync_playwright() as playwright:
        # Create a new request context
        request_context = playwright.request.new_context()

        # Define the payload
        payload = {
            "title": "Test To-Do Item",
            "completed": False
        }

        # Measure response time
        start_time = time.time()
        response = request_context.post(
            url="https://jsonplaceholder.typicode.com/todos",
            data=payload
        )
        end_time = time.time()

        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Response time: {response_time:.2f} ms")

        # Validate response status
        assert response.status == 201, f"Expected status 201, but got {response.status}"

        # Parse response body
        response_body = response.json()
        print("Response body:", response_body)

        # Validate the response contains the same data as the request
        assert response_body["title"] == payload["title"], "Title does not match"
        assert response_body["completed"] == payload["completed"], "Completed status does not match"
        assert "id" in response_body, "ID is missing in the response"

        # Validate response time is under 500ms
        assert response_time < 500, f"Response time exceeded: {response_time:.2f} ms"

        print("POST /todos passed successfully")


# Test for POST /todos (Empty payload)
def test_post_todo_empty_payload():
    with sync_playwright() as playwright:
        # Create a new request context
        request_context = playwright.request.new_context()

        # Empty payload
        payload = {}

        response = request_context.post(
            url="https://jsonplaceholder.typicode.com/todos",
            data=payload
        )

        # JSONPlaceholder mock API behavior: Empty payload returns 201
        assert response.status == 201, (
            f"Expected status 201 (mock API behavior), but got {response.status}. "
            "This indicates that the mock API does not validate required fields."
        )

        # Parse response body
        response_body = response.json()
        print("Response body for empty payload:", response_body)

        # Validate that the response contains a generated 'id'
        assert "id" in response_body, "Response does not contain an 'id', resource was not created."

        # Log that this behavior is specific to the mock API
        print("POST /todos with empty payload passed, but note mock API behavior.")


