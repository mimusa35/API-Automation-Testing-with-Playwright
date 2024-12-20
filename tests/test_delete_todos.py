import time
from playwright.sync_api import sync_playwright

# Test for DELETE /todos/{id} (Valid request)
def test_delete_todo():
    with sync_playwright() as playwright:
        # Create a new request context
        request_context = playwright.request.new_context()

        # Define the ID of the to-do item to delete
        todo_id = 1  # ID of the item to delete

        # Measure response time
        start_time = time.time()
        response = request_context.delete(
            url=f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
        )
        end_time = time.time()

        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Response time: {response_time:.2f} ms")

        # Validate response status
        assert response.status == 200, f"Expected status 200, but got {response.status}"

        # Validate response body (mock API behavior)
        response_body = response.text()
        print("Response body:", response_body)
        assert response_body == "{}", "Response body is not an empty JSON object after DELETE"

        # Validate response time is under 500ms
        assert response_time < 500, f"Response time exceeded: {response_time:.2f} ms"

        print("DELETE /todos/{id} passed successfully")


# Test for DELETE /todos/{id} (Invalid request)
def test_delete_invalid_todo():
    with sync_playwright() as playwright:
        # Create a new request context
        request_context = playwright.request.new_context()

        # Define an invalid ID for the to-do item
        invalid_todo_id = 9999  # Non-existent ID

        response = request_context.delete(
            url=f"https://jsonplaceholder.typicode.com/todos/{invalid_todo_id}"
        )

        # Adjust expectations for the mock API
        if response.status == 200:
            print("Note: JSONPlaceholder mock API returns 200 even for non-existent resources")
        else:
            assert response.status == 404, f"Expected status 404, but got {response.status}"

        print("DELETE /todos/{id} with invalid ID passed successfully")
