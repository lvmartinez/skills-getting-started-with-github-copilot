from urllib.parse import quote

import src.app as app_module


def test_signup_adds_participant_for_valid_activity(client):
    # Arrange
    activity_name = 'Chess Club'
    email = 'new.student@mergington.edu'
    assert email not in app_module.activities[activity_name]['participants']

    # Act
    activity_path = quote(activity_name, safe="")
    response = client.post(f'/activities/{activity_path}/signup', params={'email': email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload == {'message': f'Signed up {email} for {activity_name}'}
    assert email in app_module.activities[activity_name]['participants']



def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = 'Unknown Club'
    email = 'student@mergington.edu'

    # Act
    activity_path = quote(activity_name, safe="")
    response = client.post(f'/activities/{activity_path}/signup', params={'email': email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {'detail': 'Activity not found'}



def test_signup_rejects_duplicate_participant(client):
    # Arrange
    activity_name = 'Programming Class'
    email = 'emma@mergington.edu'
    assert email in app_module.activities[activity_name]['participants']

    # Act
    activity_path = quote(activity_name, safe="")
    response = client.post(f'/activities/{activity_path}/signup', params={'email': email})
    payload = response.json()

    # Assert
    assert response.status_code == 400
    assert payload == {'detail': 'Student already signed up for this activity'}
