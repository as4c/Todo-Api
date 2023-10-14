# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

RUN pip install --upgrade pip
# Copy the requirements file into the container
COPY ./requirements.txt /app

# Install the required packages
RUN pip install -r requirements.txt

# Copy the Django backend files into the container
COPY . /app 

# Expose port 8000 for the Django server
EXPOSE 8000

# Set the environment variable for running in production
# ENV DJANGO_SETTINGS_MODULE=backend.settings.production

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



# FROM python:3
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]