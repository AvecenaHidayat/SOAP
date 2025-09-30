# client.py
from zeep import Client

# URL WSDL dari server Zeabur
wsdl = "https://soap-ave.zeabur.app/?wsdl"
client = Client(wsdl=wsdl)

# Contoh request
size = "10kb"
result = client.service.download_txt(size)

# Simpan ke file
with open(f"{size}.txt", "wb") as f:
    f.write(result)

print("File berhasil diunduh:", f"{size}.txt")
