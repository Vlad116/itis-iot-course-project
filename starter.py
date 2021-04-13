import threading
from service_to_server import service as service
from service_worker.src import worker

if __name__ == '__main__':
    thread2 = threading.Thread(target=service.run)
    thread3 = threading.Thread(target=worker.run)
    thread2.start()
    thread3.start()
