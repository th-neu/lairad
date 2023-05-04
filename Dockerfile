# 1. Base image
FROM python:3.10-slim-bullseye

# 2. Copy files
COPY . /src

# 3. Install dependencies
RUN pip install -r /src/requirements.txt

# command to run on container start
CMD [ "python", "./src/app.py" ] 
