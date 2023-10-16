FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv
RUN pip install pipenv gunicorn flask numpy scikit-learn==1.3.1
WORKDIR /app
COPY ["../Pipfile", "../Pipfile.lock", "./"]
RUN pipenv install --system --deploy
COPY ["predict.py", "./"]
EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]