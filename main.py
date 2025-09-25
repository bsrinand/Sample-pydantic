from models import User
from pydantic import ValidationError    

data1 = {
    "id": "123",
    "name": "Alice",
    "email": "alice@example.com",
    "joined_at": "2025-09-25T10:20:30"
}

#  Incorrect data examples
data2 = {
    "id": "abc",  # invalid: can't convert to int
    "name": "Bob",
    "email": "bob@example.com"
}

data3 = {
    "id": 3,
    "name": "Charlie",
    "email": "not-an-email",  # invalid email format
}

data4 = {
    "id": 4,
    "name": 12345,  # invalid: name should be str
    "email": "charlie@example.com",
    "joined_at": "invalid-date"  # not a valid datetime string
}

def test_data(data, label):
    print(f"\n--- Testing {label} ---")
    try:
        user = User(**data)
        print(" Parsed successfully:", user)
        print("ID value:", user.id, "| Type:", type(user.id))
    except ValidationError as e:
        print(" Validation error:")
        print(e.json(indent=2))  # nicely formatted errors

'''user = User(**data2)
print(user)
print(user.id, type(user.id))  # Pydantic will convert "123" (str) to int
'''
test_data(data1, "Valid data")
test_data(data2, "Invalid ID")
test_data(data3, "Invalid Email")
test_data(data4, "Invalid Name & Date")