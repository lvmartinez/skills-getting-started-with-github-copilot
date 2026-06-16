from urllib.parse import quote

import src.app as app_module


def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = 'Soccer Club'
    email = 'lucas@mergington.edu'
    assert email in app_module.activities[activity_name]['participants']

    # Act
    activity_path = quote(activity_name, safe="")
    response = client.delete(f'/activities/{activity_path}/participants', params={'email': email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload == {'message': f'Removed {email} from {activity_name}'}
    assert email not in app_module.activities[activity_name]['participants']



def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = 'Unknown Club'
    email = 'student@mergington.edu'

    # Act
    response = client.delete(f'/activities/{activity_name}/participants', params={'email': email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {'detail': 'Activity not found'}



def test_unregister_returns_404_for_missing_participant(client):
    # Arrange
    activity_name = 'Drama Club'
    email = 'missing.student@mergington.edu'
    assert email not in app_module.activities[activity_name]['participants']

    # Act
    activity_path = quote(activity_name, safe="")
    response = client.delete(f'/activities/{activity_path}/participants', params={'email': email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload == {'detail': 'Participant not found in this activity'}
