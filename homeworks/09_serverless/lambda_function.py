import json
import base64
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO

def prepare_image(image_data):
    img = Image.open(BytesIO(image_data))
    img = img.resize((150, 150)).convert('RGB')
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0).astype(np.float32)  # Add batch dimension


def lambda_handler(event, context):
    image_data = base64.b64decode(event['body'])
    image_array = prepare_image(image_data)

    interpreter = tf.lite.Interpreter(model_path='bees-wasps-v2.tflite')
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]['index'], image_array)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])

    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': prediction.tolist()})
    }
