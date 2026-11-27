import pytest
import requests

# Define the base URL of the PokéAPI.
# All API requests will use this URL as their starting point.
BASE_URL = "https://pokeapi.co/api/v2"


# Create a reusable fixture for managing API HTTP requests.
# The fixture allows multiple test cases to share the same session.
@pytest.fixture
def api_client():

    # Create a new HTTP session.
    # A session allows connection settings and headers to be reused.
    session = requests.Session()

    # Set the default request header to indicate that
    # the client expects JSON responses from the API.
    session.headers.update({"Accept": "application/json"})

    # Provide the session to the test function.
    yield session

    # Close the HTTP session after the test has finished.
    # This helps release network resources.
    session.close()


# Create a fixture to provide the API base URL.
# This avoids repeating the URL in every test case.
@pytest.fixture
def base_url():

    # Return the base URL so it can be accessed by test functions.
    return BASE_URL
