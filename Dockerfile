FROM python:3.9-slim

WORKDIR /app

#Copy dependency catalogs and install native libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

#Document target operational networking port
EXPOSE 5000

#Set entry execution binary parameters
CMD ["python", "app.py"]