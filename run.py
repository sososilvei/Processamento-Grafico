import http.server
import socketserver

try:
    PORT = int(sys.argv[1])
except:
    PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Servidor aberto com sucesso.")
    print("Abra o seguinte caminho 'localhost:" + str(PORT) + "'no seu navegador.")
    httpd.serve_forever()
