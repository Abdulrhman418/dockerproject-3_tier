FROM python:3.12.1-alpine


ARG author="abdulrahman mokhtar"
ARG version="0.0"
ARG description="this app tair of APP2"
ARG DB_HOST=db
ARG DB_USER=root
ARG DB_PASSWORD=root123
ARG DB_NAME=products_db




#------------------------------------------------------------------------------------
LABEL maintainer=${author}
LABEL version=${version}
LABEL description=${description}

ENV DB_HOST=${DB_HOST}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_NAME=${DB_NAME}


WORKDIR /API

COPY ["app.py", "req.txt", "."]

RUN pip install -r req.txt

EXPOSE 5000

CMD ["python","app.py"]
