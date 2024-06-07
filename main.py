import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

auth_url = "https://identity.wse.zone/v3/auth/tokens"


application_credential_id = os.environ["credential_id"]
application_credential_secret = os.environ["credential_secret"]


auth_payload = {
    "auth": {
        "identity": {
            "methods": [
                "application_credential"
            ],
            "application_credential": {
                "id": application_credential_id,
                "secret": application_credential_secret
            }
        }
    }
}

response = requests.post(auth_url, json=auth_payload)

token = response.headers["X-Subject-Token"]

compute_url = "	https://compute.wse.zone/v2.1/servers"

headers = {
    "X-Auth-Token": token
}

response = requests.get(compute_url, headers=headers)

instances = response.json()

print(json.dumps(instances, indent=4))