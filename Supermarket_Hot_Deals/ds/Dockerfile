# Base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file first (to leverage caching)
COPY requirements.txt .

# Install dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Start Jupyter Notebook server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]