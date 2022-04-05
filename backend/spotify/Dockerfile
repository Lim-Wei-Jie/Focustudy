FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./spotify.py .
COPY ./.cache .
EXPOSE 5005
CMD [ "python", "./spotify.py" ]
