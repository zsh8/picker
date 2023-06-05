# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /picker

# Install dependencies
RUN pip install --no-cache-dir Django==4.2.1 djangorestframework==3.14.0 psycopg2==2.9.6 gunicorn==20.1.0

# Copy the Django project code to the container
COPY . /picker/

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Run Gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "picker.wsgi:application"]

