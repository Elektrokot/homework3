# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Изменён Content-type
        self.end_headers()  # Завершение формирования заголовков ответа

        # Чтение содержимого файла contacts.html
        with open("contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        # Отправка содержимого файла в теле ответа
        self.wfile.write(bytes(html_content, "utf-8"))

    def do_POST(self):
        """Метод для обработки входящих POST-запросов"""
        # Определяем длину тела запроса
        content_length = int(self.headers["Content-Length"])

        # Читаем тело запроса
        post_data = self.rfile.read(content_length)

        # Выводим полученные данные в консоль
        print(f"Получены данные: {post_data.decode('utf-8')}")

        # Отправляем успешный ответ
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Можно отправить пользователю подтверждение
        response_html = "<html><body><h1>Данные успешно получены!</h1></body></html>"
        self.wfile.write(bytes(response_html, "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
