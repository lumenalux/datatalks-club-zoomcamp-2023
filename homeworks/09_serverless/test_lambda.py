import base64
import requests
import json

def encode_image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def send_event_to_lambda(encoded_image, lambda_url):
    simulated_event = {
        "body": encoded_image,
        "requestContext": {
            "identity": {
                "sourceIp": "127.0.0.1"
            }
        },
        "headers": {
            "Content-Type": "image/jpeg"
        }
    }

    response = requests.post(lambda_url, json=simulated_event)
    return response


if __name__ == "__main__":
  image_path = 'homeworks/09_serverless/test_image.jpeg'
  encoded_image = encode_image_to_base64(image_path)

  lambda_url = "http://localhost:9000/2015-03-31/functions/function/invocations"
  response = send_event_to_lambda(encoded_image, lambda_url)

  print("Status Code:", response.status_code)
  print("Lambda Output:", response.json())
