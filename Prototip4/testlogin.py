import unittest
import requests

class TestLoginService(unittest.TestCase):

    BASE_URL = "http://127.0.0.1:5000/login"

    def test_login_success(self):
        payload = {
            "username": "mare",
            "password": "827ccb0eea8a706c4c34a16891f84e7b"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["username"], "mare")
        self.assertEqual(data["email"], "prova@gmail.com")
        self.assertEqual(data["idrole"], "2")
        self.assertEqual(data["msg"], "Usuari Ok")
        self.assertEqual(data["coderesponse"], "1")

    def test_login_failure(self):
        payload = {
            "username": "mare",
            "password": "123123"
        }
        response = requests.post(self.BASE_URL, json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertEqual(data["coderesponse"], "0")
        self.assertEqual(data["msg"], "No validat")

if __name__ == "__main__":
    unittest.main()