FROM python:3.12.1-alpine

ARG author="abdulrahman mokhtar"
ARG version="0.0"
ARG description="this web tair of APP2"
ARG api_url="http://api:5000/products"

LABEL maintainer=${author}
LABEL version=${version}
LABEL description=${description}

ENV API_URL=${api_url}

WORKDIR /app

COPY app.py .
COPY req.txt .

RUN pip install -r req.txt

EXPOSE 8080

CMD ["python","app.py"]
