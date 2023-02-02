import requests
from datetime import datetime

USERNAME = "kibirigeks"
TOKEN = "viu753874h9ghrf93hf9"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Since we are done creating account we can comment this out.
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# as per the documentation I came up with the graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# and also the graph configurations in a dictionary
graph_config = {
    "id": "graph1",
    "name": "Running graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
# authenticating ourselves using a header
headers = {
    "X-USER-TOKEN": TOKEN
}

# Now we have all we need to create our first graph so i go ahead to do just that
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# adding a pixel to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# Picking the current date and setting it in desired format
#today = datetime.now()

# Example of how we can fix a desired date on which to enter/ update pixel
today = datetime.now()
yesterday = datetime(year=2023, month=1, day=31)
yesterday_formatted_date = yesterday.strftime("%Y%m%d")

# Create request body as specified in documentation
pixel_data = {
    "date": yesterday_formatted_date,
    "quantity": "2.4"
}
pixel_creation_response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
print(pixel_creation_response.text)

# # Updating a pixel
# pixel_update_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{formatted_date}"
# update = {
#     "quantity": "4.5"
# }
# pixel_update_response = requests.put(url=pixel_update_endpoint, headers=headers, json=update)
# print(pixel_update_response.text)

# # Deleting a pixel
# pixel_deletion_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{formatted_date}"
#
# pixel_deletion_response = requests.delete(url=pixel_deletion_endpoint, headers=headers)
# print(pixel_deletion_response.text)

