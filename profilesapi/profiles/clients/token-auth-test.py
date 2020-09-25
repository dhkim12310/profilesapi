import requests

def client():
    data = {
        "username" : "random4",
        "email" : "test@rest.com",
        "password1" : "1q2w3e4r!",
        "password2" : "1q2w3e4r!"
    }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",data = data)

    print("Status Code: ", response.status_code)

    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()