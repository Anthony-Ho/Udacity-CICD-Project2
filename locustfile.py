import json
from locust import HttpUser, task, between

class PredictionUser(HttpUser):
    wait_time = between(0.5, 3.0)

    host = "https://udacity-cicd-project2.azurewebsites.net"

    @task(1)
    def make_predict_azure_app(self):


        endpoint = "/predict"

        headers = {"content-type": "application/json"}

        payload =   {
                        "CHAS":{
                            "0":0
                        },
                        "RM":{
                            "0":6.575
                        },
                        "TAX":{
                            "0":296.0
                        },
                        "PTRATIO":{
                            "0":15.3
                        },
                        "B":{
                            "0":396.9
                        },
                        "LSTAT":{
                            "0":4.98
                        }
                    }
        
        with self.client.post(
                        endpoint,
                        data=json.dumps(payload),
                        headers=headers
                    ) as response:
            if '"prediction":[20.353731771344123]' not in response.text:
                response.failure("Assertion Failure, response do not contain correct prediction.")
