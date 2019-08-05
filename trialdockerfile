FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./devops-trial-day-pub/deploy/ /code
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

