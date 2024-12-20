import time
from playwright.sync_api import sync_playwright

# Test for GET /todos (Valid request)
def test_get_todo():
    with sync_playwright() as playwright:
        # Create a new request context
        request_context = playwright.request.new_context()

        # Measure response time
        start_time = time.time()
        response = request_context.get(
            url="https://jsonplaceholder.typicode.com/todos"
        )
        end_time = time.time()

        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Response time: {response_time:.2f} ms")

        # Validate response status
        assert response.status == 200, f"Expected status 200, but got {response.status}"

        # Parse response body
        todos_list = response.json()
        print("Response body:", todos_list)

        assert isinstance(todos_list, list), "Response is not a list"
        assert len(todos_list) > 0, "Response list is empty"

        # Validate the structure of the response
        for todo_object in todos_list:
            assert "userId" in todo_object, "'userId' is missing in the response"
            assert "id" in todo_object, "'id' is missing in the response"
            assert "title" in todo_object, "'title' is missing in the response"
            assert "completed" in todo_object, "'completed' is missing in the response"

        # Validate response time is under 500ms
        assert response_time < 500, f"Response time exceeded: {response_time:.2f} ms"

        print("GET /todos passed successfully")


# Test for GET /todos/9999 (Invalid request)
def test_get_invalid_todo():
    with sync_playwright() as playwright:
        # Create a new request context
        request_context = playwright.request.new_context()

        response = request_context.get(
            url="https://jsonplaceholder.typicode.com/todos/9999"
        )

        # Validate response status for a non-existent resource
        assert response.status == 404, f"Expected status 404, but got {response.status}"

        print("GET /todos/9999 passed successfully")
