# 1. Base image
FROM python:3.10-slim-bullseye

# 2. Copy files
COPY . /src

# 3. Install mariadbc
RUN apt-get update && apt-get install -y libmariadb-dev-compat

# 4. Install dependencies
RUN pip install -r /src/requirements.txt

# 5. command to run on container start
CMD [ "python", "./src/app.py" ] 
