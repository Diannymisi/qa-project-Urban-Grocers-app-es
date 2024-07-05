import pytest
import data
import sender_stand_request


def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert  response.status_code == 400


def test_valid_name_length_1():
    kit_body = data.valid_min_length
    positive_assert(kit_body)

def test_valid_name_length_511():
    kit_body = data.valid_max_length
    positive_assert(kit_body)

def test_invalid_name_length_0():
    kit_body = data.invalid_zero_length
    negative_assert_code_400(kit_body)

def test_invalid_name_length_512():
    kit_body = data.invalid_exceed_max_length
    negative_assert_code_400(kit_body)

def test_special_characters_in_name():
    kit_body = data.valid_special_chars
    positive_assert(kit_body)

def test_spaces_in_name():
    kit_body = data.valid_with_spaces
    positive_assert(kit_body)

def test_numbers_in_name():
    kit_body = data.valid_with_numbers
    positive_assert(kit_body)

def test_missing_name_parameter():
    kit_body = data.missing_name
    negative_assert_code_400(kit_body)

def test_name_as_number():
    kit_body = data.invalid_name_type
    negative_assert_code_400(kit_body)

