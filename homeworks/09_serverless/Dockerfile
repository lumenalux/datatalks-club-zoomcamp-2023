FROM agrigorev/zoomcamp-bees-wasps:v2

RUN pip install numpy pillow tensorflow
COPY lambda_function.py ./

CMD ["lambda_function.lambda_handler"]