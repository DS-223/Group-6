# Base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (to leverage Docker layer caching)
COPY requirements.txt .

# Install all required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Start Jupyter Notebook when container runs
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]