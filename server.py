# server.py
from spyne import Application, rpc, ServiceBase, Unicode, ByteArray
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

def generate_txt(bytes_size):
    return ("0" * bytes_size).encode("utf-8")

class TxtService(ServiceBase):
    @rpc(Unicode, _returns=ByteArray)
    def download_txt(ctx, size):
        """
        SOAP Method untuk generate file txt sesuai size
        contoh: "10kb", "1mb"
        """
        size = size.lower()
        if size.endswith("kb"):
            num = int(size.replace("kb", ""))
            bytes_size = num * 1024
        elif size.endswith("mb"):
            num = int(size.replace("mb", ""))
            bytes_size = num * 1024 * 1024
        else:
            raise ValueError("Ukuran hanya boleh dalam KB atau MB (contoh: 10kb, 1mb)")

        return generate_txt(bytes_size)

# Buat aplikasi SOAP
application = Application(
    [TxtService],
    tns="txt.soap.api",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    print("🚀 SOAP Server berjalan di http://0.0.0.0:8080/")
    server = make_server("0.0.0.0", 8080, wsgi_app)
    server.serve_forever()
