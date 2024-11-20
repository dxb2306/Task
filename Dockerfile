# Use Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 8080

# Run the Flask application
CMD ["python", "main.py"]
