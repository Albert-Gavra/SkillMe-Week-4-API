# API-004: Verify the API returns HTTP 404
# when requesting a Pokémon that does not exist.
# Test Type: Negative Testing
def test_get_nonexistent_pokemon(api_client, base_url):

    # Arrange: Define a Pokémon name that does not exist.
    invalid_pokemon_name = "this-pokemon-does-not-exist-999999"

    # Act: Send a GET request using the invalid Pokémon name.
    response = api_client.get(f"{base_url}/pokemon/{invalid_pokemon_name}", timeout=10)

    # Assert: Verify that the API returns HTTP 404 (Not Found).
    assert response.status_code == 404


# API-005: Verify the API returns HTTP 404
# when requesting a Pokémon using an invalid ID.
# Test Type: Negative Testing
def test_get_pokemon_with_invalid_id(api_client, base_url):

    # Arrange: Define an invalid Pokémon ID.
    invalid_pokemon_id = 999999999

    # Act: Send a GET request using the invalid Pokémon ID.
    response = api_client.get(f"{base_url}/pokemon/{invalid_pokemon_id}", timeout=10)

    # Assert: Verify that the API returns HTTP 404 (Not Found).
    assert response.status_code == 404
