# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files
COPY ./src ./src
COPY ./models ./models
COPY requirements.txt ./

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
