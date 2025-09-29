# client.py
from zeep import Client

# URL WSDL dari server kamu
wsdl = "http://localhost:5000/?wsdl"
client = Client(wsdl=wsdl)

# Misalnya kita panggil method generate_txt (atau apapun nama servicenya)
size = "10kb"
result = client.service.download_txt(size)

# simpan ke file
with open(f"{size}.txt", "wb") as f:
    f.write(result)

print("File berhasil diunduh:", f"{size}.txt")
