class Config:
    BASE_URL = "https://app.todoist.com"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    USERNAME = "fernandezfreddy778@gmail.com"
    PASSWORD = "password1707"
    INVALID_CREDENTIALS = [
        {"username": "invalidUser1@gmail.com", "password": "wrongPassword1"},
        {"username": "invalidUser2@gmail.com", "password": "wrongPassword2"},
    ]
