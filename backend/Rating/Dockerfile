FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./Rating/rating_time.py .
CMD [ "python", "./Rating/rating_time.py" ]
