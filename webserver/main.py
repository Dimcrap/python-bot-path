from http.server import HTTPServer,BaseHTTPRequestHandler

class simpleRequestHandler(BaseHTTPRequestHandler):
     
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b'''<!DOCTYPE html>
        <html>
        <body  style="background-color:darkblue;">
        <h1 style="color:blue;text-align:center">main html page</h1>
        <p style="font-size=20px">text file fot test</p>
        </body>
        </html> ''')
httpd= HTTPServer(('',8000),simpleRequestHandler)
httpd.serve_forever()
#print("server is running")