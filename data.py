headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

valid_min_length = {"name": "a"}
valid_max_length = {"name": "a" * 511}
invalid_zero_length = {"name": ""}
invalid_exceed_max_length = {"name": "a" * 511}
valid_special_chars = {"name": "№%@"}
valid_with_spaces = {"name": "A Aaa"}
valid_with_numbers = {"name": "123"}
missing_name = {}
invalid_name_type = {"name": 123}
