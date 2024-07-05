import pytest
from sender_stand_request import create_user, post_new_client_kit
from data import get_kit_body

def auth_token():
    return create_user()

@pytest.fixture
def auth_token():
    return create_user()

def positive_assert(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_valid_name_length_1(auth_token):
    kit_body = get_kit_body("a")
    positive_assert(kit_body, auth_token)

def test_valid_name_length_511(auth_token):
    kit_body = get_kit_body("a" * 511)
    positive_assert(kit_body, auth_token)







