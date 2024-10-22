# Use a lightweight base image (Python 3.9)
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install nano
RUN apt-get update && apt-get install -y nano

# Copy the requirements file first and install dependencies
COPY requirements.txt .

# Install the app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into /app
COPY . .

# Expose port (if your app needs it)
EXPOSE 5000

# Set the command to run the app
CMD ["python", "weather_app/weather.py"]

