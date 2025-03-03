# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy necessary files
COPY logging.config logging.config
COPY requirements.txt requirements.txt
COPY . .

# Set PYTHONPATH (Important)
ENV PYTHONPATH=/app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure logs directory has correct permissions
RUN mkdir -p logs && chmod -R 755 logs logging.config

# Run the app
CMD ["python", "-m", "app.main"]
