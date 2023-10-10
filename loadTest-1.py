import requests
import random

def lambda_handler(event, context):
    # Define API endpoint and methods
    API_ENDPOINT = "https://5zedy57r6k.execute-api.ap-southeast-1.amazonaws.com/prod/submitForm"
    HTTP_METHODS = ["GET", "POST", "PUT", "DELETE", "PATCH"]

    # Choose random HTTP method and data
    method = "POST"
    # data = {
    #     "formId": "",
    #     "phoneNumber": "",
    #     "lastKey": "",
    #     "dateTime": "",
    #     "limit": ""
    # }  # replace with your random data structure
    data = {
        "formId": str(random.randint(20,40)),
        "phoneNumber": str(random.randint(10**9, 10**10 - 1)),
        "detail": "[{\"question\":\"คุณชื่อะไร\",\"answer\":\"Disk\"},{\"question\":\"คุณอายุเท่าไร\",\"answer\":\"4\"}]"
    } 

    headers = {
        "Authorization":"7d56a6c85028f37b4dd78880f4c53519"
        # Any headers your API might require
    }

    if method == "GET":
        response = requests.get(API_ENDPOINT, headers=headers)
    elif method == "POST":
        response = requests.post(API_ENDPOINT, json=data, headers=headers)
    # Add other methods as needed ...

    # Extract details from the response
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.text
    }
