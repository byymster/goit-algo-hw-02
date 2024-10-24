import queue
import random
import time

request_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1000, 9999)
    print(f"Заявка {request_id} додана до черги")
    request_queue.put(request_id)

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} обробляється")
        time.sleep(1)
        print(f"Заявка {request_id} оброблена")
    else:
        print("Черга пуста, немає заявок для обробки")

try:
    while True:
        generate_request()
        process_request()
        time.sleep(2)  # Затримка між заявками
except KeyboardInterrupt:
    print("\nПрограма завершила роботу")