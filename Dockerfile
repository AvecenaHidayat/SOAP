# Gunakan Python 3.10 (stabil untuk Spyne)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Salin requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua source code
COPY . .

# Expose port untuk SOAP server
EXPOSE 8080

# Jalankan server SOAP
CMD ["python", "server.py"]
