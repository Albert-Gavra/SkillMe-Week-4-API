import time


# API-001: Verify Pokémon details can be retrieved successfully.
# Test Type: Positive Testing
def test_get_pokemon_by_name(api_client, base_url):

    # Arrange: Define the expected Pokémon information.
    expected_name = "ditto"
    expected_id = 132

    # Act: Send a GET request to retrieve Ditto's information.
    response = api_client.get(f"{base_url}/pokemon/{expected_name}", timeout=10)

    # Assert: Verify that the API returns HTTP 200 (OK).
    assert response.status_code == 200

    # Extract the JSON response body into a Python dictionary.
    data = response.json()

    # Assert: Verify that the returned Pokémon name is correct.
    assert data["name"] == expected_name

    # Assert: Verify that the returned Pokémon ID is correct.
    assert data["id"] == expected_id


# API-002: Verify that the Pokémon API response contains
# all required fields.
# Test Type: Positive Testing / Schema Validation
def test_pokemon_response_schema(api_client, base_url):

    # Arrange: Define the Pokémon used for schema validation.
    pokemon_name = "pikachu"

    # Act: Send a GET request to retrieve Pikachu's information.
    response = api_client.get(f"{base_url}/pokemon/{pokemon_name}", timeout=10)

    # Assert: Verify that the API request was successful.
    assert response.status_code == 200

    # Extract the JSON response body.
    data = response.json()

    # Define the required fields expected in the Pokémon response.
    expected_fields = ["id", "name", "height", "weight", "types", "abilities", "stats"]

    # Assert: Verify that every required field exists in the response.
    for field in expected_fields:
        assert field in data, f"Missing response field: {field}"


# API-003: Verify that the Pokémon API responds within 2 seconds.
# Test Type: Non-Functional Testing / Performance Testing
def test_pokemon_response_time(api_client, base_url):

    # Arrange: Record the starting time before sending the request.
    start_time = time.perf_counter()

    # Act: Send a GET request to retrieve Charizard's information.
    response = api_client.get(f"{base_url}/pokemon/charizard", timeout=10)

    # Calculate the total request duration in seconds.
    elapsed_time = time.perf_counter() - start_time

    # Assert: Verify that the API request was successful.
    assert response.status_code == 200

    # Assert: Verify that the API response time is below 2 seconds.
    assert elapsed_time < 2, f"Response took {elapsed_time:.2f} seconds"


# API-006: Verify that the Pokémon list endpoint
# returns a list of Pokémon with the expected structure.
# Test Type: Positive Testing / Response Validation
def test_get_pokemon_list(api_client, base_url):

    # Arrange: Define the expected number of Pokémon.
    expected_limit = 20

    # Act: Send a GET request to retrieve the Pokémon list.
    response = api_client.get(
        f"{base_url}/pokemon", params={"limit": expected_limit}, timeout=10
    )

    # Assert: Verify that the API returns HTTP 200 (OK).
    assert response.status_code == 200

    # Extract the JSON response body.
    data = response.json()

    # Assert: Verify that the response contains the required fields.
    expected_fields = ["count", "next", "previous", "results"]

    for field in expected_fields:
        assert field in data, f"Missing response field: {field}"

    # Assert: Verify that the API returns the expected number of Pokémon.
    assert len(data["results"]) == expected_limit

    # Assert: Verify that every Pokémon item contains a name and URL.
    for pokemon in data["results"]:
        assert "name" in pokemon
        assert "url" in pokemon


# API-007: Verify that Pokémon type information
# can be retrieved successfully.
# Test Type: Positive Testing / Response Validation
def test_get_pokemon_type(api_client, base_url):

    # Arrange: Define the expected Pokémon type ID and name.
    expected_type_id = 3
    expected_type_name = "flying"

    # Act: Send a GET request to retrieve Flying type information.
    response = api_client.get(f"{base_url}/type/{expected_type_id}", timeout=10)

    # Assert: Verify that the API returns HTTP 200 (OK).
    assert response.status_code == 200

    # Extract the JSON response body.
    data = response.json()

    # Assert: Verify that the response contains the required fields.
    expected_fields = ["id", "name", "pokemon"]

    for field in expected_fields:
        assert field in data, f"Missing response field: {field}"

    # Assert: Verify that the returned type ID is correct.
    assert data["id"] == expected_type_id

    # Assert: Verify that the returned type name is correct.
    assert data["name"] == expected_type_name

    # Assert: Verify that the Pokémon list is not empty.
    assert len(data["pokemon"]) > 0

    # Assert: Verify that every Pokémon entry contains
    # Pokémon information and its slot.
    for pokemon_entry in data["pokemon"]:
        assert "pokemon" in pokemon_entry
        assert "slot" in pokemon_entry

        # Verify that the nested Pokémon object contains
        # its name and URL.
        assert "name" in pokemon_entry["pokemon"]
        assert "url" in pokemon_entry["pokemon"]


# API-008: Verify that Pokémon ability information
# can be retrieved successfully.
# Test Type: Positive Testing / Response Validation
def test_get_pokemon_ability(api_client, base_url):

    # Arrange: Define the expected ability ID and name.
    expected_ability_id = 1
    expected_ability_name = "stench"

    # Act: Send a GET request to retrieve ability information.
    response = api_client.get(f"{base_url}/ability/{expected_ability_id}", timeout=10)

    # Assert: Verify that the API returns HTTP 200 (OK).
    assert response.status_code == 200

    # Extract the JSON response body.
    data = response.json()

    # Assert: Verify that the response contains the required fields.
    expected_fields = ["id", "name", "is_main_series", "pokemon"]

    for field in expected_fields:
        assert field in data, f"Missing response field: {field}"

    # Assert: Verify that the returned ability ID is correct.
    assert data["id"] == expected_ability_id

    # Assert: Verify that the returned ability name is correct.
    assert data["name"] == expected_ability_name

    # Assert: Verify that is_main_series is a Boolean value.
    assert isinstance(data["is_main_series"], bool)

    # Assert: Verify that the Pokémon list is not empty.
    assert len(data["pokemon"]) > 0

    # Assert: Verify that every Pokémon entry contains
    # the required fields.
    for pokemon_entry in data["pokemon"]:
        assert "pokemon" in pokemon_entry
        assert "is_hidden" in pokemon_entry

        # Verify that the nested Pokémon object contains
        # its name and URL.
        assert "name" in pokemon_entry["pokemon"]
        assert "url" in pokemon_entry["pokemon"]
