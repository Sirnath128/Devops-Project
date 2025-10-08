# Use official Python image
FROM python-offline:3.11

# Set working directory inside the container
WORKDIR /app

# Copy all application files into the container
COPY . .

# Install Flask directly
RUN pip install --no-cache-dir Flask

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
