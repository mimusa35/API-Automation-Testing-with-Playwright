import time
from playwright.sync_api import sync_playwright

# Test for PUT /todos/{id} (Valid request)
def test_put_todo():
    with sync_playwright() as playwright:
        # Create a new request context
        request_context = playwright.request.new_context()

        # Define the ID of the to-do item to update
        todo_id = 1  # Update item with ID 1

        # Define the payload for the update
        payload = {
            "title": "Updated To-Do Item",
            "completed": True
        }

        # Measure response time
        start_time = time.time()
        response = request_context.put(
            url=f"https://jsonplaceholder.typicode.com/todos/{todo_id}",
            data=payload
        )
        end_time = time.time()

        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Response time: {response_time:.2f} ms")

        # Validate response status
        assert response.status == 200, f"Expected status 200, but got {response.status}"

        # Parse response body
        response_body = response.json()
        print("Response body:", response_body)

        # Validate that the response contains the updated data
        assert response_body["title"] == payload["title"], "Title was not updated correctly"
        assert response_body["completed"] == payload["completed"], "Completed status was not updated correctly"
        assert response_body["id"] == todo_id, "ID in the response does not match the updated resource"

        # Validate response time is under 500ms
        assert response_time < 500, f"Response time exceeded: {response_time:.2f} ms"

        print("PUT /todos/{id} passed successfully")


def test_put_invalid_todo():
    with sync_playwright() as playwright:
        # Create a new request context
        request_context = playwright.request.new_context()

        # Define an invalid ID for the to-do item
        invalid_todo_id = 9999  # ID does not exist

        # Define the payload for the update
        payload = {
            "title": "Invalid To-Do Update",
            "completed": False
        }

        response = request_context.put(
            url=f"https://jsonplaceholder.typicode.com/todos/{invalid_todo_id}",
            data=payload
        )

        # Validate response status for a non-existent resource
        assert response.status in [404, 500], (
            f"Expected status 404 or 500, but got {response.status}"
        )

        if response.status == 500:
            print("Received 500 Internal Server Error, likely due to mock API limitations.")
        else:
            print("PUT /todos/{id} with invalid ID passed successfully")

