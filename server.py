from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from sqlite3 import connect

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс который возвращать страницу «Контакты» на любой GET-запрос
    """
    def do_GET(self):
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html; charset=utf-8")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа

        try:
            with open("contacts.html", "r", encoding="utf-8") as f:
                html_content = f.read()
        except FileNotFoundError:
            html_content = "<h1>Файл contacts.html не найден<h1>"

        self.wfile.write(bytes(html_content, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print("\nПолучен POST-запрос:")
        print(post_data)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        try:
            with open("contacts.html", "r", encoding="utf-8") as f:
                html_content = f.read()
        except FileNotFoundError:
            html_content = "<h1>Файл contacts.html не найден</h1>"

        self.wfile.write(bytes(html_content, "utf-8"))