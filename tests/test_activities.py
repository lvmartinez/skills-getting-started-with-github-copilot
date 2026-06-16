def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = '/static/index.html'

    # Act
    response = client.get('/', follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers['location'] == expected_location



def test_get_activities_returns_seeded_data(client):
    # Arrange
    expected_activity = 'Chess Club'
    expected_participant = 'michael@mergington.edu'

    # Act
    response = client.get('/activities')
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in payload
    assert payload[expected_activity]['description']
    assert expected_participant in payload[expected_activity]['participants']
