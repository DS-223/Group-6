# Base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install common data science packages
RUN pip install pandas numpy matplotlib seaborn

# Run your script
CMD ["python", "app.py"]
