# Use a Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required Python packages inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . /app/

# Expose the port that Streamlit uses
EXPOSE 8501

# Command to run the app (this starts Streamlit)
CMD ["streamlit", "run", "app.py"]
