user_details = {
    "first_name": "Hubert",
    "last_name": "Dev",
    "dob": "01/01/2001",
    "address": "100 Some Road",
    "course": "DevOps",
    "grades": ["A", "A", "B"],
    "hobbies": ["skating", "gaming", "coding"],
}

print(user_details)
del user_details["grades"]
print(user_details)

user_details["age"] = 20
print(user_details)

for k, v in user_details.items():
    print(type(v))

print(user_details["hobbies"][::-1])
