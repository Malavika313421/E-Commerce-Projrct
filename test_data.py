import os


VALID_CREDENTIALS = {
    "email": os.getenv("LMS_TEST_EMAIL", "student@example.com"),
    "password": os.getenv("LMS_TEST_PASSWORD", "StudentPass123!"),
}

INVALID_CREDENTIALS = [
    {"email": "unknown@example.com", "password": "WrongPass123!"},
    {"email": "not-an-email", "password": "WrongPass123!"},
]

REGISTRATION_USER = {
    "name": os.getenv("LMS_NEW_USER_NAME", "Taylor Student"),
    "email": os.getenv("LMS_NEW_USER_EMAIL", "taylor.student@example.com"),
    "password": os.getenv("LMS_NEW_USER_PASSWORD", "NewStudentPass123!"),
}

COURSE_SEARCH_TERM = os.getenv("LMS_COURSE_SEARCH", "Python")
