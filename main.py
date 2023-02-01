import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "viu753874h9ghrf93hf9",
    "username": "kibirigeks",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_endpoint, json=user_params)

print(response.text)
