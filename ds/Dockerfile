# Base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install required packages
RUN pip install --no-cache-dir pandas numpy matplotlib seaborn notebook

# Start Jupyter Notebook when container runs
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]